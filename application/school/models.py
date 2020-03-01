import string
import random
from django.db import models
from .enum import SexEnum, NationalityEnum


class School(models.Model):
    name = models.CharField(max_length=20)
    maximum_student = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return self.name


class StudentQuerySet(models.QuerySet):

    def create(self, **kwargs):
        if not ('id' in kwargs and kwargs['id']):
            kwargs['id'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
        return super(StudentQuerySet, self).create(**kwargs)


class __StudentManager(models.Manager):
    pass


StudentManager = __StudentManager.from_queryset(StudentQuerySet)


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1, choices=SexEnum.choices())
    nationality = models.CharField(max_length=20, choices=NationalityEnum.choices(), default=NationalityEnum.THAI)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    objects = StudentManager()

    def save(self, **kwargs):
        if not self.id:
            self.id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(20)])
        super(Student, self).save(**kwargs)

    def __str__(self):
        return "{} : {} {}".format(self.id, self.first_name, self.last_name)
