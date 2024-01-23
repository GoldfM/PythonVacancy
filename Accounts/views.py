from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from Accounts.forms import *
from Accounts.models import *
from Accounts.apiHH import *

from datetime import datetime
class Home(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        page_info = ImagesPages.objects.all().get(name_page='Главная')
        return render(request, 'main_page.html', {'images': page_info})

class Actual(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        page_info = ImagesPages.objects.all().get(name_page='Восстребованность')
        return render(request, 'actual.html', {'images': page_info})

class Geopos(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        page_info = ImagesPages.objects.all().get(name_page='География')
        return render(request, 'geopos.html', {'images': page_info})

class Skills(View):
    #paginate_by = 6
    def get(self, request, *args, **kwargs):
        page_info = ImagesPages.objects.all().get(name_page='Навыки')
        return render(request, 'skills.html', {'images': page_info})
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
