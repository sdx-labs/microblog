from django.urls import path, include
from . import views
from .views import PostUpdateView, PostDeleteView, register, CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/new/', views.create_post, name='post-form'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html')),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register')
]

