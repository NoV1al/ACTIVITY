from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import student_id, grade, section, teacher_profile, subjects
from .forms import StudentForm, SubjectForm, GradeForm, TeacherForm, SectionForm, StudentRegisterForm, StudentLoginForm, StudentEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages



app_name = 'online_enrollment'



def student_list(request):
    students = student_id.objects.all()
    return render(request,'student.html', {'students':students})

def grade_list(request):
    grado = grade.objects.all()
    return render(request,'grado.html', {'grado':grado})

def section_list(request):
    sections = section.objects.all()
    return render(request,'seksyon.html', {'sections':sections})


def teacher_list(request):
    guro = teacher_profile.objects.all()
    return render(request,'guro.html', {'guro':guro})

def subject_list(request):
    subject = subjects.objects.all()
    return render(request,'SUBJECT.html', {'subject':subject})

# __________________________________________________________________________________________________


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})


def edit_student(request, pk):
    student = student_id.objects.get(stu_id=pk)  # use stu_id, not id
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit_student.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})


def edit_subject(request, pk):
    subject = get_object_or_404(subjects, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'edit_subject.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade')
    else:
        form = GradeForm()
    return render(request, 'add_grade.html', {'form': form})


def edit_grade(request, pk):
    grade_obj = get_object_or_404(grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade_obj)
        if form.is_valid():
            form.save()
            return redirect('grade')
    else:
        form = GradeForm(instance=grade_obj)
    return render(request, 'edit_grade.html', {'form': form})
def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section')
    else:
        form = SectionForm()
    return render(request, 'add_section.html', {'form': form})


def edit_section(request, pk):
    sec = get_object_or_404(section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=sec)
        if form.is_valid():
            form.save()
            return redirect('section')
    else:
        form = SectionForm(instance=sec)
    return render(request, 'edit_section.html', {'form': form})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})


def edit_teacher(request, pk):
    teacher = get_object_or_404(teacher_profile, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'edit_teacher.html', {'form': form})

# ___________________________________________________________
from .forms import StudentLoginForm

def student_login(request):
    if request.method == 'POST':
        email = request.POST.get('stu_email')
        password = request.POST.get('password')

        try:
            student = student_id.objects.get(stu_email=email)
        except student_id.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('student_login')

        if student.stu_pass == password:
            # Save student ID in session
            request.session['student_id'] = student.stu_id  # save stu_id instead of PK

            # Redirect to profile page with stu_id parameter
            return redirect('student_profile', stu_id=student.stu_id)
        else:
            messages.error(request, "Invalid email or password")
            return redirect('student_login')

    form = StudentLoginForm()
    return render(request, 'student_login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            stu = form.save(commit=False)
            stu.stu_pass = form.cleaned_data['password']  # save password correctly
            stu.save()
            messages.success(request, "Account created!")

            # Redirect to the profile of the newly registered student
            return redirect('student_profile', stu_id=stu.stu_id)
    else:
        form = StudentRegisterForm()

    return render(request, 'student_register.html', {'form': form})

def student_logout(request):
    request.session.flush()  # clears all session data
    return redirect('student_login')

from .models import student_id

def student_profile(request, stu_id):
    # Optional: redirect to login if session doesn't exist
    if not request.session.get('student_id'):
        return redirect('student_login')

    student = get_object_or_404(student_id, stu_id=stu_id)
    return render(request, 'student_profile.html', {'student': student})


def dashboard(request):
    # Only logged-in students can access
    if 'student_id' not in request.session:
        return redirect('student_login')

    return render(request, 'dashboard.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import student_id  # <-- use your actual model name
from .forms import StudentEditForm

def student_edit(request, stu_id):
    student = get_object_or_404(student_id, stu_id=stu_id)
    if request.method == "POST":
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile', stu_id=student.stu_id)
    else:
        form = StudentEditForm(instance=student)

    return render(request, 'student_edit.html', {'form': form, 'student': student})
