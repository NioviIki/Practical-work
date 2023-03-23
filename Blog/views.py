from django.urls import reverse_lazy
from django.views import generic
from .models import Posts
from .forms import CreatePostForm
from django.contrib.auth import mixins


class CreatePosts(mixins.LoginRequiredMixin, generic.FormView):
    template_name = 'Blog/create_post_view.html'
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:create_post")

    def form_valid(self, form):
        Posts.objects.create(owner=self.request.user, text=form.cleaned_data["text"])
        return super().form_valid(form)


class UpdatePosts(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'Blog/update_posts_view.html'
    model = Posts
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:list_posts")

    def get_queryset(self, *args, **kwargs):
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