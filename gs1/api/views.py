from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
# Model Object - Single Student Data

def student_detail(request, pk):
    #complex data - model object
    stu = Student.objects.get(id=pk)
    #convert complex data into native python object
    serializer = StudentSerializer(stu)
    #convert to json
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data)

#Query Set - All Student Sata
def student_list(request):
    #complex data - model object
    stu = Student.objects.all()
    #convert complex data into native python object
    serializer = StudentSerializer(stu, many=True)
    #convert to json
    # json_data = JSONRenderer().render(serializer.data)

    # return HttpResponse(json_data, content_type='application/json')

    return JsonResponse(serializer.data, safe=False)