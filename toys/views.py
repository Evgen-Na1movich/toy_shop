from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.checks import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page

from toys.models import Category


@method_decorator(cache_page(5), name='dispatch')
    #кэшіруем старонку
class CategoriesView(View):
    def get(self, request):
        data = {'title': 'Крама цацак', 'cats': Category.objects.all()}
        return render(request, 'toys/index.html', context=data)


def index(request):  # HttpRequest
    data = {'title': 'Крама цацак'}
    return render(request, 'toys/main.html', context=data)
    # return HttpResponse('Страница приложения toys.')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Старонка не знойдзена</h1')


class Login(View):
    def get(self, request):
        context = {'form': AuthenticationForm(), 'title': 'login'}
        return render(request, 'toys/login.html', context)

    def post(self, request):
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
            return redirect('home')


def logout_func(request):
    logout(request)
    return redirect('home')


class Register(View):

    def get(self, request):
        context = {'form': UserCreationForm(), 'title': 'register'}
        return render(request, 'toys/register.html', context)

    def post(self, request):
        rf = UserCreationForm(data=request.POST)
        if rf.is_valid():
            rf.save()
            return redirect('login')
        messages.error(request, rf.errors)
        return redirect('register')
