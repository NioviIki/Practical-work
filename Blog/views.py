from django.urls import reverse_lazy
from .tasks import add_to_comment, add_to_post
from django.views import generic
from .models import Posts, Comments
from .forms import CreatePostForm, CreateCommentForm
from django.contrib.auth import mixins


class CreatePosts(mixins.LoginRequiredMixin, generic.FormView):
    template_name = 'Blog/create_post_view.html'
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:create_post")

    def form_valid(self, form):
        add_to_post.apply_async(args=[str(self.request.user),
                                form.cleaned_data["text"],
                                form.cleaned_data["subject"]])


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
        add_to_comment.apply_async(args=[str(self.request.user),
                                         form.cleaned_data["comment"],
                                         self.kwargs['pk']])
        return super().form_valid(form)


