from django.urls import reverse_lazy
from django.views import generic
from .models import Posts
from .forms import CreatePostForm
from django.contrib.auth import mixins


class CreatePost(mixins.LoginRequiredMixin, generic.FormView):
    template_name = 'Blog/create_post_view.html'
    form_class = CreatePostForm
    success_url = reverse_lazy("Blog:create_post")

    def form_valid(self, form):
        Posts.objects.create(user=self.request.user, text=form.cleaned_data["text"])
        return super().form_valid(form)
