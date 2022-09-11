import re
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, borrow
from .forms import UserForm

# Create your views here.



def home(request):
    users = User.objects.all()
    context = {'users' : users}
    return render(request, 'home.html', context)


def login_or_create(request):
    form = UserForm()
    users = User.objects.values()
    NumberUserList = [int(user['Student_number']) for user in users]
    if request.method == 'POST':
        if request.POST['Student_number'] != '':
            if int(request.POST['Student_number']) in NumberUserList: #이미 회원가입된 학번이고,   
                this_user = User.objects.get(Student_number = int(request.POST['Student_number'])) #회원가입된, 이 학번을 가진 사람에 대한 정보
                if request.POST['Student_password'] == str(this_user.Student_password): # 패스워드가 일치하면,
                    context = {'user_Student_number' : this_user.Student_number}
                    return render(request, 'umbrella.html', context) # umbrella.html사이트로 허가한 후 접속
                else :
                    context = {'exception': 1}
                    return render(request, 'exception.html', context) # 잘못 입력하셨습니다 페이지 띄우고, 해당 패이지는 1초후 다시 전 페이지로 돌아감
            elif request.POST['Student_password'] != '':
                form = UserForm(request.POST) # 가입되지 않은 회원이면 회원가입
                if form.is_valid():
                    form.save()
                    context = {'exception': 0}
                    return render(request, 'exception.html', context)
            else : 
                context = {'exception': 1}
                return render(request, 'exception.html', context)
        else : 
            context = {'exception': 1}
            return render(request, 'exception.html', context)
    context = {'form' : form}
    return render(request, 'login.html', context)

def umbrella_borrow(request, Snum):
    umbs = borrow.objects.filter(borrowed = False)
    user_borrowed = borrow.objects.filter(borrowed_by = Snum)
    if len(user_borrowed) == 0:
        if len(umbs) != 0:
            umb = umbs[0]
            umb.borrowed = True
            umb.borrowed_by = Snum
            umb.save()
            context = {'umb' : umb, 'borrower' : Snum}
        else : 
            context = {'exception': 2}
            return render(request, 'exception.html', context)
    else : 
        context = {'exception': 3, 'user' : Snum}
        return render(request, 'exception.html', context)
    return render(request, 'umbrella_borrow.html', context)

def umbrella_return(request, Snum):
    umbs = borrow.objects.filter(borrowed_by = Snum)
    if len(umbs) != 0:
        umb = umbs[0]
        umb.borrowed = False
        umb.borrowed_by = 0
        umb.save()
        context = {'umb' : umb, 'borrower' : Snum}
    else : 
        context = {'exception': 4}
        return render(request, 'exception.html', context)
    return render(request, 'umbrella_return.html', context)