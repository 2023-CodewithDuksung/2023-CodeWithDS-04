from django.contrib.auth import update_session_auth_hash, get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.checks import messages
from django.shortcuts import render, redirect


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm) :

    class Meta(UserChangeForm.Meta) :
        model = get_user_model()
        fields = ('email', 'username')

def change_password(request):
  if request.method == "POST":
    form = PasswordChangeForm(request.user, request.POST)
    if form.is_valid():
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Password successfully changed')
      return redirect('profile')
    else:
      messages.error(request, 'Password not changed')
  else:
    form = PasswordChangeForm(request.user)
  return render(request, 'change_password.html',{'form':form})