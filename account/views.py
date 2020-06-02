from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Teacher,Student
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(username = email, password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("profile",user.username)
    return render(request,"login.html")

def signup(request):
    type = request.GET.get("type",None)
    email = request.GET.get("email",None)
    request.session["email"] = email
    if type == "student":
        return render(request,"student.html")
    elif type == "teacher":
        return render(request,"teacher.html")
    else:
        return render(request,"signup.html")

def teacher_signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        cname = request.POST["cname"]
        password = request.POST["password"]
        sub = request.POST["sub"]
        
        try: 
            user = User.objects.create_user(username=email,first_name = name , password= password)
            user.save()
            teacher = Teacher.objects.create(user=user,college=cname,branch=sub)
            teacher.save()

            return redirect("login")
        except:
            return render(request,"teacher.html")

    return render(request,"teacher.html")

def student_signup(request):
    if request.method == "POST":
        email = request.POST["email"]
        name = request.POST["name"]
        cname = request.POST["cname"]
        password = request.POST["password"]
        sem = request.POST["sem"]
        sub = request.POST["sub"]
        
        try: 
            user = User.objects.create_user(username=email,first_name = name , password= password)
            user.save()
            student = Student.objects.create(user=user,college=cname,sem=sem,branch=sub)
            student.save()

            return redirect("login")
        except:
            return render(request,"student.html")
    return render(request,"student.html")

def logout(request):
    auth.logout(request)
    return redirect("login")
    


def profile(request,slug):
    return render(request,"profile.html",{"name":slug})
