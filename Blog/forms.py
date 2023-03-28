from django import forms

from .models import Comments, Posts


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
            'text': forms.Textarea,
            'synopsis': forms.Textarea,
        }
        fields = ('subject', 'synopsis', 'text', 'is_published', 'image',)


class AdminPostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        widgets = {
            'text': forms.Textarea,
            'synopsis': forms.Textarea
        }
        fields = ('owner', 'synopsis', 'text', 'subject', 'image')


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


class ContactToAdminForm(forms.Form):
    subject = forms.CharField(max_length=30)
    message = forms.CharField(max_length=200)
