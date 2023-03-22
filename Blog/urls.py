from django.urls import path

from . import views
app_name = 'Blog'

urlpatterns = [
    path('', views.CreatePost.as_view(), name='create_post')
]

