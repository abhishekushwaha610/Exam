from django.contrib import admin

from .models import *

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Options)
admin.site.register(Result)
# admin.site.register(Exam)