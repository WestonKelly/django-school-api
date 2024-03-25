from rest_framework import serializers
from .models import Grade

class GradeAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'