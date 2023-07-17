from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32, null=True)
    password = models.CharField(max_length=64, null=True)
    age = models.IntegerField(null=True)
    sex = models.IntegerField(default=0, null=True)


class Department(models.Model):
    title = models.CharField(max_length=16)


class Role(models.Model):
    name = models.CharField(max_length=16)


# 数据库 insert语句
Department.objects.create(title="销售部")
