from rest_framework import viewsets

from .models import Student, University
from .serializers import UniversitySerializer, StudentSerializer

# Create your views here.


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
