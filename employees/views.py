from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def dashboard(request):
     if not request.user.is_superuser:
        return redirect('/accounts/profile/')
     employees = Employee.objects.all()
     return render(request, 'dashboard.html', {'employees': employees})

@login_required
def add_employee(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        department = request.POST.get('department')
        salary = request.POST.get('salary')

        Employee.objects.create(
            name=name,
            email=email,
            department=department,
            salary=salary
        )

        return redirect('/')

    return render(request, 'add_employee.html')

@login_required
def edit_employee(request, id):
    emp = Employee.objects.get(id=id)

    if request.method == "POST":
        emp.name = request.POST.get('name')
        emp.email = request.POST.get('email')
        emp.department = request.POST.get('department')
        emp.salary = request.POST.get('salary')
        emp.save()

        return redirect('/')

    return render(request, 'edit_employee.html', {'emp': emp})

@login_required
def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('/')

def register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')
    return render(request,'register.html')

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')



