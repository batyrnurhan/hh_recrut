from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from teachers.views import TeacherAPIList, TeacherAPIUpdate, TeacherAPIDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/teachers/', TeacherAPIList.as_view()),
    path('api/v1/teachers/<int:pk>/', TeacherAPIUpdate.as_view()),
    path('api/v1/teachersdelete/<int:pk>/', TeacherAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]