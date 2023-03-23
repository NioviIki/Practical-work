from django import forms
from .models import Posts, Comments

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('text', 'is_published')


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comment': forms.Textarea,
        }
        fields = ('comment', )


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('owner', 'text', 'subject')
