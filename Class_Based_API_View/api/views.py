from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status

# Create your views here.
class StudentAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id = id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, format=None):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def put(self, request, pk, format=None):
        stu = Student.objects.get(pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated'})
        return Response(serializer.errors)
    def patch(self, request, pk, format=None):
        stu = Student.objects.get(pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated'})
        return Response(serializer.errors)
    def delete(self, request, pk, format=None):
        stu = Student.objects.get(pk)
        stu.delete()
        return Response({'msg': 'Data Deleted'})

        