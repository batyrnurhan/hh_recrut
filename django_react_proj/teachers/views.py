from rest_framework import generics, viewsets
from rest_framework.views import APIView
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from django.forms import model_to_dict

##vid to est kak smotretsia budet

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 

#class TeacherAPIList(generics.ListCreateAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer

#class TeacherAPIUpdate(generics.UpdateAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer

#class TeacherAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer