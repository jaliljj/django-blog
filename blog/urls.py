from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('create_post/', views.create_post, name='create_post'),
    path('api/posts/', views.post_list, name='post_list'),
    path('api/posts/<int:pk>/', views.post_detail, name='post_detail'),
]