from django.shortcuts import render
# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from usuario.forms import SignUpForm

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView, TemplateView, RedirectView


# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

def RegistroMedico(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.is_medical=True
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'homeMedico.html')
    else:
        # form = UserCreationForm()
        form = SignUpForm(request.POST)
    return render(request, 'signupMedico.html', {'form': form})



def RegistroPaciente(request):
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request, 'homePaciente.html')
    else:
        # form = UserCreationForm()
        form = SignUpForm(request.POST)
    return render(request, 'signupPaciente.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)
            if user.is_medical == True:
                # return redirect('home')
                return render(request, 'homeMedico.html')
            else:
                return render(request, 'homePaciente.html')
                # return HttpResponseRedirect('homePaciente.html')
            
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})