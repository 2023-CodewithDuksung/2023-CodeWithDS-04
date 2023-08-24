from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from team_board.models import Board
from share_info.models import Info

def mypage(request):
    my_team=Board.objects.filter(author=request.user)
    my_info=Info.objects.filter(author=request.user)
    return render(request, 'mypage.html', {
            'my_team' : my_team,
            'my_info' : my_info,
    })
    
def signup(request):  # 회원가입 함수
    if request.method == 'POST':  # 회원가입 정보 입력 후 가입하기 클릭시
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form })


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('main')
    else:
        form= AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('main')


@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('main')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'change_password.html', context)