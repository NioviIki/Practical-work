from django.urls import path

from . import views
app_name = 'Blog'

urlpatterns = [
    path('', views.CreatePosts.as_view(), name='create_post'),
    path('update/<int:pk>', views.UpdatePosts.as_view(), name='update_post'),
    path('list/', views.ListPost.as_view(), name='list_posts'),
    path('list/<int:pk>/', views.PostDetail.as_view(), name='detail_post'),
    path('list/<int:pk>/comment/', views.CreateComment.as_view(), name='comment')
]

