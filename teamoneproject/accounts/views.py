from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

# make_password : 괄호 안에 들어간 문자열 암호화

def register(request):
    if request.method == "POST":
            username = request.POST.get['username', None]
            password = request.POST.get['password', None]
            confirm_pw = request.POST.get['confirm_pw', None]

            regi_data = {}

            if not (username and password and confirm_pw):
                regi_data['error'] = "빈 칸을 채워주세요."
            elif password != confirm_pw:
                regi_data['error'] = "비밀번호를 확인해주세요."
            else:
                user = User(username=username, password=make_password(password))
                user.save()

                return render(request, 'main.html', regi_data)
    
    else:
        return render(request, 'signup.html')