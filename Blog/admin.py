from django.contrib import admin

from .models import Posts
from .forms import PostsForm

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('subject', 'owner', 'date')
    list_filter = ['date']
    form = PostsForm
    search_fields = ['owner', 'date', 'text', 'subject']
    date_hierarchy = 'date'
    list_per_page = 20
