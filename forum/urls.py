from . import views
from django.urls import path 

urlpatterns = [
    path('<slug:slug>/', views.post_detail, name="post_detail"),
    path('profile/', views.ProfileList.as_view(), name='profile'),
    path('', views.PostList.as_view(), name='home'),
]
