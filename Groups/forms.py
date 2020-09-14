from django import forms
from .models import Group, Student
from django.core.exceptions import ValidationError

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'faculty']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'second_name', 'photo', 'group_id']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'group_id': forms.Select(attrs={'class': 'form-control'}),
                    }
