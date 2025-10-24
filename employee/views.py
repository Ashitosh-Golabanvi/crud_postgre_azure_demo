from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee

# Template-based views
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            job_title=request.POST['job_title'],
            salary=request.POST['salary']
        )
        return redirect('employee_list')
    return render(request, 'employee/form.html')

def employee_update(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.job_title = request.POST['job_title']
        employee.salary = request.POST['salary']
        employee.save()
        return redirect('employee_list')
    return render(request, 'employee/form.html', {'employee': employee})

def employee_delete(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')
