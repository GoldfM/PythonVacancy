"""Cyberfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('', Home.as_view(), name='home'),
    path('profile/<slug:slug>', Profile.as_view(), name='profile'),
    path('welcome/', welcome, name='welcome'),
    path('form', wtfForm, name='form'),
    path('profile/<slug:profile_slug>/project/<slug:post_slug>', VacancyView.as_view(), name='project'),
    path('profile/project/edit-project/<slug:slug>', VacancyUpdateView.as_view(), name='editVacancy'),
    path('profile/project/add-project', addVacancy.as_view(), name='addVacancy'),
    path('form1/<name>/<surname>/<sursurname>', wtfForm1, name='form1'),
    path('profile/<slug:slug>/edit', ProfileUpdateView.as_view(), name='editProfile'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('unsubscribe/', UnsubscribeView.as_view(), name='unsubscribe'),
    path('my-subscriptions', MySubscribtions.as_view(), name='subscriptions'),
    path('deleteVacancy/', DeleteVacancy.as_view(), name='deleteVacancy'),
    path('rateVacancy/', RateVacancy.as_view(), name='rateVacancy'),
]
urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

