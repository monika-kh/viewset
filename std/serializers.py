from rest_framework import serializers

from .models import Student, University


class StudentSerializer(serializers.ModelSerializer):
    # university_name = serializers.StringRelatedField()

    class Meta:
        model = Student
        # fields = ("id", "first_name", "last_name")
        fields = "__all__"

    def to_representation(self, instance):
        # represent university name, but for post method use college id
        rep = super(StudentSerializer, self).to_representation(instance)
        rep["university_name"] = instance.university_name.name
        return rep


class UniversitySerializer(serializers.ModelSerializer):
    # ForeignKey in student model
    student = StudentSerializer(many=True, read_only=True)
    # student=related_name
    # student=serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = University
        fields = "__all__"
