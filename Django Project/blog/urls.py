from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", views.blog_index, name="blog_index"),
    path("post/<int:pk>/", views.blog_detail, name="blog_detail"),
    path("category/<str:category>/", views.blog_category, name="blog_category"),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='blog_index'), name='logout'),
    path('register/', views.register, name='register'),
    path("post/new/", views.create_post, name="create_post"),
    path("like/<int:pk>/", views.like_post, name="like_post"),
    path("comment/<int:pk>/", views.submit_comment, name="submit_comment"),
]