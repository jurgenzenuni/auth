from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from appname import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
