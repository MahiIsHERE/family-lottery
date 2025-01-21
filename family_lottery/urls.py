from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from lottery.views import register

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('', include('lottery.urls')),
]
