import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from Two.models import Student


def index(request):
    a = 100
    students = [1,2,4,6,8,9]
    return render(request, "index.html", locals())


def add(request):
    student = Student()
    student.s_name = 'Jerry-%d' % random.randrange(10000)
    student.s_age = random.randrange(100)
    student.save()
    return HttpResponse("add students %s success " %student.s_name)


def get(request):
    people = Student.objects.all()
    return render(request,"get.html",locals())