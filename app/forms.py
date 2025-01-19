from django import forms
from .models import Student
from django.core.exceptions import ValidationError

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'grade', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email
