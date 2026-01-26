from django.urls import path
from . import views

urlpatterns=[
    path('', views.dashboard),
    path('add/', views.add_employee),
    path('edit/<int:id>/', views.edit_employee),
    path('delete/<int:id>/', views.delete_employee),
    path('register/', views.register),
    path('accounts/profile/', views.profile),
]