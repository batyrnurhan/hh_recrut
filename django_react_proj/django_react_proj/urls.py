from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from teachers.views import TeacherAPIList, TeacherAPIUpdate, TeacherAPIDestroy

from materials.views import MaterialAPIList, MaterialAPIDestroy, MaterialAPIUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    #materials api
    path('api/v1/materials/', MaterialAPIList.as_view()),
    path('api/v1/materials/<int:pk>/', MaterialAPIUpdate.as_view()),
    path('api/v1/material_delete/<int:pk>/', MaterialAPIDestroy.as_view()),
    #teachers api -- gonna delete
    #path('api/v1/drf-auth/', include('rest_framework.urls')),
    #path('api/v1/teachers/', TeacherAPIList.as_view()),
    #path('api/v1/teachers/<int:pk>/', TeacherAPIUpdate.as_view()),
    #path('api/v1/teachersdelete/<int:pk>/', TeacherAPIDestroy.as_view()),
    
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]