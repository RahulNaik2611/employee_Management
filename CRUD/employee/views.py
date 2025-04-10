from django.shortcuts import render, redirect, get_object_or_404
from .form import EmployeeForm
from .models import Employee

# Create View
def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm()
    return render(request, 'create.html', {'form': form})


# List View
def emp_list(request):
    employees = Employee.objects.all()
    return render(request, 'list.html', {'employees': employees})


# Update View
def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form})


# Delete View (with confirmation page)
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect('list')
    return render(request, 'delete.html', {'employee': employee})  # Confirmation page
