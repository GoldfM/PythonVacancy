from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model

class Vacancy(models.Model):
    slug = models.SlugField(verbose_name='Слаг', unique=False)
    name = models.CharField(max_length=50, db_index=True, verbose_name="Название")
    salary_from = models.FloatField()
    salary_to = models.FloatField()
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

class Skill(models.Model):
    name = models.CharField(max_length=40, verbose_name="Навык")
    def __str__(self):
        return self.name



def user_directory_path(instance, filename):
    return 'page_image/{0}/{1}'.format(instance.name_page, filename)
class ImagesPages(models.Model):
    name_page = models.CharField(max_length=30, verbose_name='Название страницы')
    image1 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото1")
    image2 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото2")
    image3 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото3")
    image4 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото4")
    image5 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото5")
    image6 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото6")
    image7 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото7")
    image8 = models.ImageField(upload_to=user_directory_path, blank=True, verbose_name="Фото8")

    def __str__(self):
        return self.name_page

