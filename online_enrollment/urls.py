from django.urls import path
from . import views

urlpatterns = [
    # LIST VIEWS
    path('subject/', views.subject_list, name="subject"),
    path('grade/', views.grade_list, name="grades"),
    path('section/', views.section_list, name="section"),
    path('teacher/', views.teacher_list, name="teacher"),
    path('student/', views.student_list, name="student"),

    # ADD VIEWS
    path('add_student/', views.add_student, name='add_student'),
    path('add_section/', views.add_section, name='add_section'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('add_grade/', views.add_grade, name='add_grade'),
    path('add_teacher/', views.add_teacher, name='add_teacher'),

    # EDIT VIEWS
    path('edit_student/<str:pk>/', views.edit_student, name='edit_student'),  # <-- change here
    path('edit_section/<int:pk>/', views.edit_section, name='edit_section'),
    path('edit_subject/<int:pk>/', views.edit_subject, name='edit_subject'),
    path('edit_grade/<int:pk>/', views.edit_grade, name='edit_grade'),
    path('edit_teacher/<int:pk>/', views.edit_teacher, name='edit_teacher'),

    # HOME + AUTH
    path('', views.student_login, name="student_login"),
    path('register/', views.register_view, name="student_register"),
    path('logout/', views.student_logout, name="student_logout"),
    path('profile/', views.student_profile, name='student_profile'),
    path('dashboard/', views.dashboard, name="dashboard"),

# urls.py
    path('student/<str:stu_id>/edit/', views.student_edit, name='student_edit'),
    path('student/<str:stu_id>/', views.student_profile, name='student_profile'),




]
