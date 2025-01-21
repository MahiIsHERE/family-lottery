from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.box_list, name='box_list'),
    path('box/<int:box_id>/', views.box_detail, name='box_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout view

]
