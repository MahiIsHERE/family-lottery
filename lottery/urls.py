from django.urls import path
from . import views

urlpatterns = [
    path('', views.box_list, name='box_list'),
    path('box/<int:box_id>/', views.box_detail, name='box_detail'),
    path('register/', views.register, name='register'),  # New registration URL
]
