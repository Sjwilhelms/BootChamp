from . import views
from django.urls import path 

urlpatterns = [
    path('create-post/', views.create_post_view, name='create_post'),
    path('create-profile/', views.create_profile_view, name='create_profile'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name="comment_edit"),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name="comment_delete"),
    
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('', views.PostList.as_view(), name='home'),
]
