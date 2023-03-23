from django import forms
from .models import Posts

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('text', 'is_published')


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('owner', 'text')