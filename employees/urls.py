from django.urls import path
from . import views

urlpatterns=[
    path('',views.Dashboard),
    path('add/',views.add_employee),
    path('edit/<int:id>/',views.edit_employee),
    path('delete/<int:id>/',views.delete_employee),
]