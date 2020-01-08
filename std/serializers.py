from .models import *
from rest_framework import serializers



class StudentSerializer(serializers.ModelSerializer):
    university_name = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = "__all__"

class UniversitySerializer(serializers.ModelSerializer):                         #ForeignKey in student model
    student = StudentSerializer(many=True,read_only=True)                        #student=related_name

    #student=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = University
        fields = "__all__"


