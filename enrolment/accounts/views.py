from django.shortcuts import render, redirect

# 로그인하기위한 import
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            # 유저생성
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'])
            # 로그인함수
            auth.login(request, user)

            # 로그인후에 이동할 페이지입력
            # return redirect('~~')
            return render(request, 'accounts/home.html')

    # 유저생성, 로그인 실패시 이 페이지에 머무르게
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 디비상의 유저와 입력된 정보를 확인함
        user = auth.authenticate(request, username = username, password = password)

        if user is not None:
            auth.login(request, user)

            # return redirect('~~')
            return render(request, 'accounts/home.html')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)

        return redirect('login')
    else:
        return render(request, 'accounts/login.html')

