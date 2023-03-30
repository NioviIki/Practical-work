from core import settings

from django.contrib.auth import mixins
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactToAdminForm, CreateCommentForm, CreatePostForm, RegisterForm
from .models import Comments, Posts
from .tasks import send_massage


class RegisterFormView(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy("Blog:list_posts")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class CreatePosts(mixins.LoginRequiredMixin, generic.FormView):
    template_name = 'Blog/create_post_view.html'
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:create_post")

    def form_valid(self, form):
        Posts.objects.create(owner=User.objects.get(username=self.request.user),
                             text=form.cleaned_data["text"],
                             subject=form.cleaned_data["subject"],
                             synopsis=form.cleaned_data['synopsis'],
                             image=form.cleaned_data['image'],
                             is_published=form.cleaned_data['is_published']
                             )
        send_massage.apply_async(args=['new message',
                                       settings.EMAIL_HOST_USER, 'New Post'])
        return super().form_valid(form)


class UpdatePosts(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'Blog/update_posts_view.html'
    model = Posts
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:list_posts")

    def get_queryset(self):
        return Posts.objects.filter(pk=self.kwargs['pk']).filter(owner=self.request.user)


class ListPost(generic.ListView):
    template_name = 'Blog/list_post_view.html'
    model = Posts
    paginate_by = 15

    def get_queryset(self):
        return Posts.objects.select_related('owner').filter(is_published=True)


class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'Blog/post_detail_view.html'

    def get_queryset(self):
        return Posts.objects.select_related('owner').prefetch_related('comments_set').\
            filter(pk=self.kwargs['pk']).filter(is_published=True)


class CreateComment(generic.FormView):
    form_class = CreateCommentForm
    template_name = 'Blog/create_comment_view.html'

    def form_valid(self, form):
        self.success_url = reverse_lazy('Blog:detail_post', kwargs={'pk': self.kwargs['pk']})
        Comments.objects.create(author=self.request.user,
                                comment=form.cleaned_data["comment"],
                                post=Posts.objects.get(pk=self.kwargs['pk'])
                                )
        send_massage.apply_async(args=['new message',
                                       settings.EMAIL_HOST_USER,
                                       'new message'])
        send_massage.apply_async(args=['new message',
                                       Posts.objects.get(pk=self.kwargs['pk']).owner.email,
                                       self.success_url])
        return super().form_valid(form)


class PublicProfile(generic.DetailView):
    model = User
    template_name = 'registration/public_profile_view.html'

    def get_queryset(self):
        return User.objects.prefetch_related('posts_set').filter(pk=self.kwargs['pk'])


class UpdateProfile(mixins.LoginRequiredMixin, generic.UpdateView):
    model = User
    template_name = 'registration/update_profile.html'
    fields = ('username', 'last_name', 'first_name', 'email')

    def get_queryset(self):
        return User.objects.filter(pk=self.kwargs['pk']).filter(username=self.request.user)

    def form_valid(self, form):
        self.success_url = reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})
        return super().form_valid(form)


class ContactToAdmin(mixins.LoginRequiredMixin, generic.FormView):
    form_class = ContactToAdminForm
    template_name = 'Blog/contact_to_admin.html'
    success_url = reverse_lazy('Blog:feedback')

    def form_valid(self, form):
        text = f'{form.cleaned_data["message"]} \n By {self.request.user}'
        send_massage.apply_async(args=[form.cleaned_data['subject'],
                                       settings.EMAIL_HOST_USER,
                                       text]
                                 )
        return super().form_valid(form)
