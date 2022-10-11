from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher 
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')