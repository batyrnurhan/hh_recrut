from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Category, Teacher
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TeacherSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action


##vid to est kak smotretsia budet

class TeacherAPIList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class TeacherAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)


class TeacherAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAdminOrReadOnly,)
