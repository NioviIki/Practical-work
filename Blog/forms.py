from django import forms
from .models import Posts, Comments

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('text', 'is_published')

class AdminPostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
          'text': forms.Textarea,
        }
        fields = ('owner', 'text', 'subject')



class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comment': forms.Textarea,
        }
        fields = ('comment', )


class AdminCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        widgets = {
            'comment': forms.Textarea,
        }
        fields = ('comment', 'author', 'is_published')


