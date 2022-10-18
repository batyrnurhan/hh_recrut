from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import CategoryOfMaterial, Material
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import MaterialSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from rest_framework.decorators import action


##vid to est kak smotretsia budet

class MaterialAPIList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MaterialAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAuthenticated,)
    #authentication_classes = (TokenAuthentication,)


class MaterialAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = (IsAdminOrReadOnly,)
