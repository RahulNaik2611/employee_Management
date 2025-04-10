from django.db import models

class Employee(models.Model):
    emp_id = models.CharField(max_length=20, unique=True)  # Ensures each employee ID is unique
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)  # Usually, emails are unique for each employee
    emp_cont = models.CharField(max_length=20, verbose_name="Contact Number")

    def __str__(self):
        return f"{self.emp_name} ({self.emp_id})"
