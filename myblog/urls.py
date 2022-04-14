from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('signup',views.signup, name='signup'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('blogs/<str:pk>',views.blogs, name='blogs'),
    path('blogs/<str:pk>/addcomment',views.add_comment, name='addcomment'),
    path('join', views.join, name='join')
  
   
]