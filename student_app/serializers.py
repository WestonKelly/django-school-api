from rest_framework import serializers
from subject_app.serializers import SubjectAllSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Student
from subject_app.models import Subject

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'student_email', 'locker_number']

class StudentAllSerializer(serializers.ModelSerializer):
    subjects = SubjectAllSerializer(many=True)

    class Meta:
        model = Student
        fields = ['name', 'student_email', 'personal_email', 'locker_number', 'locker_combination', 'good_student', 'subjects']

    # def get_subjects(self, instance):
    #     subjects = instance.subjects
# {"id": 1, "subject_name": "Python", "professor": "Professor Adam"}
        
    def get_subjects(self,instance):
        subjects = instance.subjects.all()
        # list comphresion
        ser_subjects = [{"id": x.id, "subject_name": x.subject_name, "professor": x.professor} for x in subjects]
        return ser_subjects