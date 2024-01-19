from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model

class Vacancy(models.Model):
    slug = models.SlugField(verbose_name='Слаг', unique=False)
    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")
    salary_from = models.FloatField()
    salary_to = models.FloatField()
    salary_currency = models.ForeignKey('Currency', on_delete = models.PROTECT)
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['id']


class SkillVacancy(models.Model):
    vacancy = models.ForeignKey('Vacancy', verbose_name='Фото проекта', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', verbose_name='Фото проекта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
        ordering = ['id']

class Currency(models.Model):
    name = models.CharField(max_length=40)
    value = models.FloatField()
    def __str__(self):
        return self.name
class Skill(models.Model):
    name = models.CharField(max_length=40, verbose_name="Навык")
    def __str__(self):
        return self.name



