from django.contrib import admin

# Register your models here.
from akirachix.models import Students
admin.site.register(Students)

from akirachix.models import Teachers
admin.site.register(Teachers)

from akirachix.models import Courses
admin.site.register(Courses)

