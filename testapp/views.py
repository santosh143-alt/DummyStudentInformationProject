from django.shortcuts import render
from testapp.models import Student
# Create your views here.
def student_view(request):
    student_list = Student.objects.all()
    my_dict = {'student_list': student_list}
    return render(request,'testapp/data.html',my_dict)

def studenttable_view(request):
    student_list = Student.objects.all()
    my_dict = {'student_list': student_list}
    return render(request,'testapp/tablesformat.html',my_dict)