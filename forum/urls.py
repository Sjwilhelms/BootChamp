from . import views
from django.urls import path

urlpatterns = [
    path('profile/', views.Profile.as_view(), name='profile'),
    path('', views.PostList.as_view(), name='home'),
]
