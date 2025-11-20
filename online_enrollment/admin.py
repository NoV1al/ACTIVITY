from django.contrib import admin
from .models import  student_id, subjects , grade , section , teacher_profile

admin.site.register (student_id)
admin.site.register (subjects)
admin.site.register (grade)
admin.site.register (section)
admin.site.register (teacher_profile)

# Register your models here.
