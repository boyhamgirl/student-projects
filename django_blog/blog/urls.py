from django.urls import path
from . import views


urlpatterns = [
path('signup/', views.signup, name='signup'),


path('posts/', views.post_list, name='post_list'),
path('posts/new/', views.post_create, name='post_create'),
path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
path('posts/<slug:slug>/edit/', views.post_update, name='post_update'),
path('posts/<slug:slug>/delete/', views.post_delete, name='post_delete'),
path('posts/<slug:slug>/publish/', views.post_publish, name='post_publish'),


path('hx/posts/<int:pk>/inline-title/', views.hx_post_title_inline, name='hx_post_title_inline'),
path('hx/search/', views.hx_search, name='hx_search'),
path('hx/<slug:slug>/comments/create/', views.hx_comment_create, name='hx_comment_create'),
]
