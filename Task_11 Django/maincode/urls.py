from django.urls import path
from . import views

urlpatterns = [
    path('', views.transaction_create, name='transaction_create'),
    path('success/', views.transaction_success, name='transaction_success'),
]
