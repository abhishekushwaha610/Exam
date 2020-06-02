from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('login',views.login,name="login" ),
    path('signup',views.signup,name="signup" ),
    path('logout',views.logout,name="logout" ),
    path('teacher-signup',views.teacher_signup,name="teacher-signup" ),
    path('student-signup',views.student_signup,name="student-signup" ),
    # path('docs/', include("sphinxdoc.urls")),
]
