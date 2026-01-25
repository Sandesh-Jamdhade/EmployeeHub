from django.shortcuts import render,redirect
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def Dashboard(request):
    employees= Employee.objects.all()
    return render(request,'Dashboard.html',{'employees':employees})

@login_required
def add_employee(request):
    if request.method == "POST":
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            department=request.POST['department'],
            salary=request.POST['salary']
        )
        return redirect('/')
    return render(request,'add_employee.html')

@login_required
def edit_employee(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        emp.name=request.POST['name']
        emp.email=request.POST['email']
        emp.department=request.POST['department']
        emp.salary=request.POST['salary']
        emp.save()
        return redirect('/')
    return render(request,'edit_employee.html',{'emp':emp})

@login_required
def delete_employee(request,id):
    Employee.objects.get(id=id).delete()
    return redirect('/')
