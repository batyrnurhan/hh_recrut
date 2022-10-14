from django.contrib import admin
from django.urls import path, re_path
from teachers.views import TeacherAPIView,TeacherAPIList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/teacherslist', TeacherAPIList.as_view()),
    path('api/v1/teacherslist/<int:pk>', TeacherAPIList.as_view()),
]