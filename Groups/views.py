from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Group, Student
from django.views.generic import View
from .forms import GroupForm, StudentForm


def groups_list(request):
    groups = Group.objects.all()
    return render(request, 'Groups/groups_list.html', context = {'groups':groups})

def students_list(request):
    students = Student.objects.all()
    return render(request, 'Groups/students_list.html', context = {'students':students})

class StudentDetail(View):
    def get(self, request, slug):
        student = get_object_or_404(Student, slug__iexact=slug)
        return render(request, 'Groups/student_detail.html',context={'student':student})

class GroupDetail(View):
    def get(self, request, slug):
        group = get_object_or_404(Group, slug__iexact=slug)
        students = Student.objects.filter(group_id=group)
        return render(request, 'Groups/group_detail.html', context={'students': students})

class GroupCreate(View):
    def get(self, request):
       form = GroupForm()
       return render(request, 'Groups/group_create.html', context={'form': form})

    def post(self, request):
        bound_form = GroupForm(request.POST)

        if bound_form.is_valid():
            new_group = bound_form.save()
            return redirect('groups_list')
        return render(request, 'Groups/group_create.html', context={'form': bound_form})

class StudentCreate(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'Groups/student_create.html', context={'form': form})

    def post(self, request):
        bound_form = StudentForm(request.POST, request.FILES)

        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect('students_list')
        return render(request, 'Groups/student_create.html', context={'form': bound_form})

class GroupUpdate(View):
    def get(self, request, slug):
        group = Group.objects.get(slug__iexact=slug)
        bound_form = GroupForm(instance=group)
        return render(request, 'Groups/group_update.html', context={'form': bound_form, 'group': group})

    def post(self, request, slug):
        group = Group.objects.get(slug__iexact=slug)
        bound_form = GroupForm(request.POST, instance=group)

        if bound_form.is_valid():
            new_group = bound_form.save()
            return redirect(new_group)
        return render(request, 'Groups/group_update.html', context = {'form':bound_form, 'group':group})

class StudentUpdate(View):
    def get(self, request, slug):
        student = Student.objects.get(slug__iexact=slug)
        bound_form = StudentForm(instance=student)
        return render(request, 'Groups/student_update.html', context={'form': bound_form, 'student': student})

    def post(self, request, slug):
        student = Student.objects.get(slug__iexact=slug)
        bound_form = StudentForm(request.POST, request.FILES, instance=student)

        if bound_form.is_valid():
            new_student = bound_form.save()
            return redirect(new_student)
        return render(request, 'Groups/student_update.html', context = {'form':bound_form, 'student':student})

class GroupDelete(View):
    def get(self, request, slug):
        group = Group.objects.get(slug__iexact = slug)
        return render(request, 'Groups/group_delete.html', context = {'group': group})

    def post(self, request, slug):
        group = Group.objects.get(slug__iexact=slug)
        group.delete()
        return redirect('groups_list')

class StudentDelete(View):
    def get(self, request, slug):
        student = Student.objects.get(slug__iexact = slug)
        return render(request, 'Groups/student_delete.html', context = {'student': student})

    def post(self, request, slug):
        student = Student.objects.get(slug__iexact=slug)
        student.delete()
        return redirect('students_list')
