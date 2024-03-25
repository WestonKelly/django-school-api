from rest_framework import serializers
from .models import Subject

class SubjectAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'