from django.http import HttpResponse
from django.shortcuts import render,redirect
from AdminApp.models import Category, Question
from userApp.models import UserInfo, allResult

# Create your views here.
def home(request):
    # return HttpResponse('hello')
    cats = Category.objects.all()
    return render(request,'master.html',{"cats":cats}) 

def quizStartPage(request,id):
    cats = Category.objects.all()
    cat = Category.objects.get(id=id)
    return render(request,'quizStartPage.html',{"cats":cats,'cat':cat}) 

def TestPage(request,id):
    # return HttpResponse('hello')
    cats = Category.objects.all()
    cat = Category.objects.get(id=id)
    questions = Question.objects.filter(category=cat)
    if request.method == 'POST':
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            u = str(q.id)
            try:
                x = request.POST[u]
            except:
                x = "1"
            if q.ans == x:
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            # 'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
            }
        if ("uname" in request.session):
            user = UserInfo.objects.get(username = request.session["uname"])
            result = allResult()
            result.user = user
            result.category = cat  
            result.correct = correct
            result.total = total
            result.per = percent
            result.save()
        return render(request,'result.html',{'context':context,"cats":cats,"cat":cat})
        
    else:
        return render(request,'testPage.html',{'questions':questions,'cat':cat})

def login(request):
    cats = Category.objects.all()
    if request.method == "GET":
        return render(request,"login.html",{'cats':cats})    
    else:
        uname = request.POST['uname']
        pwd = request.POST['pwd']
        try:
            user = UserInfo.objects.get(username = uname,password = pwd)
        except:
            massage = 'invalid user and password'
            return render(request,"login.html",{'cats':cats,'massage':massage})
        else:
            request.session["uname"] = uname
            return redirect(home)
            
def logout(request):
    request.session.clear()
    return redirect(home)

def signUp(request):
    cats = Category.objects.all()
    if request.method == "GET":
        return render(request,"signUp.html",{'cats':cats})    
    else:
        uname = request.POST["uname"]
        pwd = request.POST['pwd']
        email = request.POST['email']

        try:
            findUname = UserInfo.objects.get(username = uname)
        except:
            user = UserInfo(uname,pwd,email)
            user.save()
            return redirect(home)
        else:
            massage = "User Name already exists"
            return render(request,"signUp.html",{'cats':cats,'massage':massage})

def performance(request):
    uname = request.session['uname']
    user = UserInfo.objects.get(username=uname)
    cats = Category.objects.all()
    results = allResult.objects.filter(user=user)
    return render(request,'allResult.html',{'cats':cats,'results':results})

def viewResult(request,id):
    cats = Category.objects.all()
    cat = Category.objects.get(id=id)
    questions = Question.objects.filter(category=cat)
    return render(request,"viewResult.html",{'cats':cats,'questions':questions})
