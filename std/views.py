from django.shortcuts import render
from rest_framework import viewsets
from . models import *
from . serializers import *

# Create your views here.
class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer

    # def post(self, request):
    #     breakpoint()
    #     return self.create(request)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
