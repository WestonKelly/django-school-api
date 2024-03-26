from django.shortcuts import render
from .models import Student
from .serializers import StudentAllSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class All_students(APIView):

    def get(self, request):
        students = Student.objects.all()
        ser_students = StudentAllSerializer(students, many=True)
        return Response(ser_students.data)

