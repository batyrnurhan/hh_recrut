from django.contrib import admin
from django.urls import path, re_path, include
from teachers.views import TeacherViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'teachers', TeacherViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]