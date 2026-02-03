from django.shortcuts import render, redirect
import requests

BACKEND = "http://127.0.0.1:8000"

def login_view(request):
    error = None

    if request.method == "POST":
        resp = requests.post(f"{BACKEND}/login/", data=request.POST)

        if resp.status_code == 200:
            data = resp.json()

            if data.get("is_admin"):
                return redirect("dashboard")
            else:
                return redirect("profile")

        error = "Invalid username or password"

    return render(request, "login.html", {"error": error})


def register_view(request):
    error = None

    if request.method == "POST":
        resp = requests.post(f"{BACKEND}/register/", data=request.POST)

        if resp.status_code == 200:
            return redirect("login")

        error = "User already exists"

    return render(request, "register.html", {"error": error})


def dashboard(request):
    response = requests.get(f"{BACKEND}/employees/")
    employees = response.json()
    return render(request, "dashboard.html", {"employees": employees})


def add_employee(request):
    if request.method == "POST":
        requests.post(f"{BACKEND}/employees/create/", data=request.POST)
        return redirect("dashboard")
    return render(request, "add_employee.html")


def edit_employee(request, id):
    if request.method == "POST":
        requests.put(f"{BACKEND}/employees/update/{id}/", data=request.POST)
        return redirect("dashboard")
    response = requests.get(f"{BACKEND}/employees/{id}/")
    employee = response.json()

    return render(request, "edit_employee.html", {"employee": employee})



def delete_employee(request, id):
    requests.delete(f"{BACKEND}/employees/delete/{id}/")
    return redirect("dashboard")


def profile(request):
    return render(request, "profile.html")


def logout_view(request):
    return redirect("login")
