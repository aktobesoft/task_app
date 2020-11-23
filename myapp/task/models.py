from django.db import models
from django.shortcuts import reverse

class task(models.Model):
    title = models.CharField(verbose_name="Наименование задачи", max_length=150)
    description = models.CharField(verbose_name="Описание задачи", max_length=350)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail_url', kwargs={'id':self.id})

class Person(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
