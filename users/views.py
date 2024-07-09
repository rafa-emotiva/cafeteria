# views.py
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import UserRegisterForm

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('list_product')  
        return render(request, self.template_name, {'form': form})
