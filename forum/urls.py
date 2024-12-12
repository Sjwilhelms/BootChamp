from . import views
from django.urls import path 

urlpatterns = [
    path('create-post/', views.create_post_view, name='create_post'),
    path('post/edit/<slug:slug>/', views.edit_post_view, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post_view, name='delete_post'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name="comment_edit"),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name="comment_delete"),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('', views.PostList.as_view(), name='home'),
]
