from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import Exam,Question
from .forms import Question_form,Question_content
from uuid import uuid4

def add_exam(request):
    if request.method == "POST":
        exam = request.POST["ename"]
        sem = request.POST["sem"]
        startDate = request.POST["startDate"]
        startTime = request.POST["startTime"]
        endTime = request.POST["endTime"]
        if exam and sem:
            request.user.teacher.exam_set.create(name=exam,sem=sem,start_date=startDate,start_time=startTime,end_time=endTime,unique=uuid4().hex)
        return redirect("profile",request.user.username)
    return render(request,"add-exam.html",)

def add_question(request,sha,task):
    if request.method == "POST":
        exam = Exam.objects.get(unique=sha)
        if task == "add":
            form = Question_form(request.POST,request.FILES)
            if form.is_valid():
                question = form.cleaned_data["content"]
                num = request.POST.get("hidden",None)
                options_dict =  {}
                for o in range(int(num)+1):
                    key = request.POST.get(f"option-{o+1}",None)
                    if key:
                        options_dict[ key] = request.POST.get(f"checkbox{o+1}",None)
                quest = exam.question_set.create(question=question)
                quest.save()
                for option,value in options_dict.items():
                    if value == "on":
                        quest.options_set.create(option=option,is_true=True).save()
                    else:
                        quest.options_set.create(option=option,is_true=False).save()

            # print(options_dict,question,num,o)
            return redirect("add-question","add",sha)
    exam = Exam.objects.get(unique=sha)
    return render(request,"add-question.html",{
        "exam":exam,
        "questionForm" : Question_form()
        # "Questions" : exam.question_set.all().reverse()
    })

def delete_question(request):
    sha = request.GET["sha"]
    qid = request.GET["qid"]
    exam = Exam.objects.get(unique=sha)
    question = exam.question_set.get(id=qid)
    question.delete()

    return HttpResponse(True)
    # print('deleted')
    # return redirect("add-question","add",sha)

def edit_question(request,sha,id):
    exam = Exam.objects.get(unique=sha)
    question = Question.objects.get(id=id)
    if request.method == "POST":
        question = Question_content(request.POST,instance=question)
        # print("valid",question)
        if question.is_valid():
            quest =  question.save(commit = True)
            num = request.POST.get("hidden",None)
            for o in quest.options_set.all():
                o.delete()
            
            for o in range(int(num)+1):
                option = request.POST.get(f"option-{o+1}",None)
                value = request.POST.get(f"checkbox{o+1}",None)
                print(option,value)
                if option:
                    if value == "on":
                        quest.options_set.create(option=option,is_true=True).save()
                    else:
                        quest.options_set.create(option=option,is_true=False).save()
            return redirect("add-question","add",sha)

    content = Question_content(instance=question)
    return render(request,"edit-question.html",{
        'exam' : exam,
        "content" : content,
        'question' : question
    })