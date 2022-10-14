from rest_framework import generics
from rest_framework.views import APIView
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.response import Response
from django.forms import model_to_dict
from django.http import Http404
##vid to est kak smotretsia budet


class TeacherAPIList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherAPIView(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request):
        t = Teacher.objects.all()
        return Response({'posts': TeacherSerializer(t, many=True).data})

    def post(self, request):
        serializer = TeacherSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)

        if not pk:
            return Response({"error": "METHOD PUT not allowed"})

        try:
            instance = Teacher.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesnt exists"})

        serializer = TeacherSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, pk, **kwargs):
        event = self.get_object(pk)
        event.delete()
        return Response({"post": "deleted"})