from cProfile import label
from dataclasses import field
from socket import fromshare
from tkinter import Widget
from turtle import textinput
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'last_name', 'first_name', 'email', 'course', 'gpa' ]
        labels = {
            'student_number' :'Student Number',
             'last_name': 'First name', 
             'first_name': 'Last Name', 
             'email': 'Email', 
             'course': 'Course', 
             'gpa': 'GPA'
        }
        widgets = {
            'student_number' : forms.NumberInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'course':forms.TextInput(attrs={'class': 'form-control'}), 
            'gpa': forms.NumberInput(attrs={'class': 'form-control'})
        }