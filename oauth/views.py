from django.shortcuts import render
from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import * 
import binascii
from hashlib import sha256
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, LoginView
from django.urls import reverse_lazy
from .models import User
from django.http.response import HttpResponseNotFound


def acc(request,id):
    user = User.objects.get(id=id)
    return render(request,'registration/account.html', {'user':user})

def edit(request, id):
    try:
        user = User.objects.get(id=id)
        form1 = ChangeForm(instance=user)
        if request.method == "POST":
            form = ChangeForm(request.POST,request.FILES,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('acc',user.id)
        else:
            context = {'user':user,
                        'form':form1}
            return render(request, "registration/edit.html", context)
    except User.DoesNotExist:
        return HttpResponseNotFound("<img src='https://http.cat/403'>")
    


class LoginView(LoginView):
    form_class = LoginForm
    
    def get_success_url(self) -> str:
        return reverse_lazy('acc',kwargs={'id':self.request.user.id})

    def form_invalid(self, form):
        print(form)
        return self.render_to_response(self.get_context_data(form_request=form))

class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = 'login'

    def post(self,request,*args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully registered')
            return redirect('login')
        else:
            
            return render(request,self.template_name,{'form_request':form,'form':form})


def Logout(request):
    logout(request)
    return redirect('/')
def delete_account(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('/')


class Passwordresetview(PasswordResetView):
    form_class = ResetPasswordForm
    template_name: str = 'registration/password_reset_form.html'
 

class Passwordchangeview(PasswordResetConfirmView):
    form_class = ConfirmPasswordForm
    template_name: str = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('login')