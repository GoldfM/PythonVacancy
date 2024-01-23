import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.http import HttpResponseRedirect, QueryDict, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from scipy.constants import slug

from Accounts.forms import *
from Accounts.models import *
from Accounts.apiHH import *

from datetime import datetime
class Home(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        return render(request, 'main_page.html')

class Actual(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        return render(request, 'actual.html')

class Geopos(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        return render(request, 'geopos.html')

class Skills(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        return render(request, 'skills.html')
class LastVacancies(ListView):
    #paginate_by = 6
    model = Vacancy
    template_name = "main_page.html"
    context_object_name = "vacancies"

    def get_context_data(self, *, object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Главная страница"
        return context

    def get_queryset(self):
        vacancies = Vacancy.objects.all()

        if self.request.method == 'GET':
            pass


        return vacancies

class LastVacancies(View):
    def get(self, request, *args, **kwargs):
        last_vacs = get_data_vacancies(str(datetime.now())[:10], 15)
        return render(request, 'last_vac.html', context={'vacancies': last_vacs})
