from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from Three.models import Student, Grade


def index(request):
    three_index = loader.get_template("three_index.html")
    context = {
        "student_name": "TOM",
    }
    # 下边用render的时候，没有提示。
    return HttpResponse(three_index.render(context=context))


def get_grade(request):
    student = Student.objects.get(pk=4)
    # 获取了一个学生的所有信息，如下是获取了grade这个qurry。
    grade = student.s_grage
    return HttpResponse("grade:%s" % grade.g_name)


def get_stu(request):
    grade = Grade.objects.get(g_name="linux")
    # 通过班级反向查所有学生
    students = grade.student_set.all()
    for i in students:
        print(i.s_name,i.s_grage.g_name)
    # return render(request,"get_stu.html")
    return HttpResponse("GET IT!")