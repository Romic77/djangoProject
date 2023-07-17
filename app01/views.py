import json

from django.shortcuts import render, HttpResponse, redirect
from app01 import models


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def tpl(request):
    name = "张三"
    roles = ["超级管理员", "CEO", "CFO"]
    my_dict = {"name": "zhangsan", "slary": 12345}

    data_list = [{"name": "zhangsan1", "slary": 12345}, {"name": "zhangsan2", "slary": 12345}, {"name": "zhangsan3", "slary": 12345}]

    str = json.dumps(data_list)

    return render(request, "tpl.html", {"name": name, "roles": roles, "my_dict": my_dict, "data_list": data_list, "jsonStr": str})


def user_login(request):
    if request.method == "GET":
        return render(request, "user_login.html")

    print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")
    if username == "333" and password == "333":
        return HttpResponse("登录成功")

    return render(request, "user_login.html", {"message": "登录失败，用户名和密码错误", "code": "50001"})


def orm(request):
    # 添加部门
    # models.Department.objects.create(title="销售部门")
    # models.Department.objects.create(title="IT部门")
    # models.Department.objects.create(title="运营部门")
    # 根据id删除部门
    # department = models.Department
    # department.objects.filter(id=1).delete()

    # department.objects.filter(id=2).update(title="我也母鸡啊")

    # 添加用户信息
    # models.UserInfo.objects.create(username="zhangsan", password="123456", age=18)

    # 查询
    user_list = models.UserInfo.objects.all()
    for user in user_list:
        print(user.username + "：" + user.password)

    return HttpResponse("orm成功")


def info_list(request):
    # 获取数据库中所有的用户信息
    data_list = models.UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    age = request.POST.get("age")

    # 创建用户信息
    models.UserInfo.objects.create(username=username, password=password, age=age)
    return render(request, "info_list.html")
