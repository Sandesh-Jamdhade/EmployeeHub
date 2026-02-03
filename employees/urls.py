from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add/", views.add_employee, name="add_employee"),
    path("edit/<int:id>/", views.edit_employee, name="edit_employee"),
    path("delete/<int:id>/", views.delete_employee, name="delete_employee"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile, name="profile"),

]

