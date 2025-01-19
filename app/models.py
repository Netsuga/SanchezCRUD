from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    grade = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

