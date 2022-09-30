from pydoc import resolve
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):
    context = Student.objects.all()
    return render(request, 'student/index.html', {'students':context})

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            nstudent_number = form.cleaned_data['student_number']
            dfirst_name = form.cleaned_data['first_name']
            nlast_name = form.cleaned_data['last_name']
            nemail = form.cleaned_data['email']
            ncourse = form.cleaned_data['course']
            ngpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = nstudent_number,
                first_name = dfirst_name,
                last_name = nlast_name,
                email = nemail,
                course = ncourse,
                gpa = ngpa
            )

            new_student.save()
            return render(request, 'student/add_student.html', {
                'form':StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
        return render(request, 'student/add_student.html', {
            'form':StudentForm()
        }) 


def edit_student(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'student/edit_student.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, 'student/edit_student.html', {
            'form':form,
        })

def delete_student(request, id):
    if request.method == "POST":
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))