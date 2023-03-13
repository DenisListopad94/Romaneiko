from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import ListView

from .models import *
import json
from django.views.generic.edit import CreateView


def main(request):
    return render(request, 'main.html')


def add_user(request):
    if request.method == 'POST':
        print(request.POST)
        Users.objects.create(name=request.POST['name'],
                             surname=request.POST['surname'],
                             age=request.POST['age'],
                             sex=request.POST['sex'],
                             phone=request.POST['phone'],
                             hobbies=request.POST['hobbies'],
                             msg=request.POST['msg'],
                             favorite_place_name=request.POST['favorite_place_name'],
                             work=request.POST['work'],
                             photo=request.POST['photo'],

                             )
        redirect('/app/main')
    return render(request, 'add_user.html')

# class add_user(CreateView):
#     template_name = 'form_for_user.html'
#     model = 'Users'
#     fields = ['name', 'surname', 'age', 'sex', 'phone', 'hobbies', 'msg', 'favorite_place_name', 'work', 'photo']
#     success_url = reverse_lazy("main")


class MyView(ListView, PermissionRequiredMixin):
    template_name = "form.html"
    model = Users
    context_object_name = "users"


def host(request):
    users = Users.objects.all()
    return render(request, 'host.html', {"users": users})
