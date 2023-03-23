from django.contrib import admin

from .models import Posts, Comments
from .forms import AdminPostsForm, AdminCommentForm

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'owner', 'date')
    list_filter = ['date']
    form = AdminPostsForm
    search_fields = ['owner', 'date', 'text', 'subject']
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    form = AdminCommentForm
    list_display = ('author', 'date', 'is_published', 'comment')

