from django.urls import path
from .views import create_employee,update_employee,emp_list,delete_employee

urlpatterns = [
    path("",emp_list,name='list'),
    path("create/",create_employee,name='create'),
    path("update/<int:pk>",create_employee,name='update'),
    path("delete/<int:pk>", delete_employee,name='delete')
]
