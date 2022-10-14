from rest_framework import generics, viewsets, mixins
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Category, Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action
##vid to est kak smotretsia budet

class TeacherViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet
):
    #queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Teacher.objects.all()[:3]
        
        return Teacher.objects.filter(pk=pk)


    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

#class TeacherAPIList(generics.ListCreateAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer

#class TeacherAPIUpdate(generics.UpdateAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer

#class TeacherAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = Teacher.objects.all()
#  serializer_class = TeacherSerializer