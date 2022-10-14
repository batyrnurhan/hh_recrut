import io
from rest_framework import serializers
from .models import Teacher
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('pk', 'name', 'surname', 'email', 'phone', 'document', 'cat', 'is_staff')
