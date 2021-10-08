from django.urls import path
from app import views

urlpatterns = [
    path('produto/', views.produto_list),
    path('produto/<int:pk>/', views.produto_detail),
]