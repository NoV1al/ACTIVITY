from django import forms 
from .models import student_id, subjects, section, teacher_profile, grade
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = student_id
        fields = ['stu_id', 'stu_name', 'stu_email', 'stu_con', 'password']

class StudentLoginForm(forms.Form):
    stu_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)



class StudentForm (forms.ModelForm):
    class Meta: 
        model = student_id
        fields = '__all__'

class SubjectForm (forms.ModelForm):
    class Meta: 
        model = subjects
        fields = '__all__'


class SectionForm (forms.ModelForm):
    class Meta: 
        model = section
        fields = '__all__'

class TeacherForm (forms.ModelForm):
    class Meta: 
        model = teacher_profile
        fields = '__all__'

class GradeForm (forms.ModelForm):
    class Meta: 
        model = grade
        fields = '__all__'



