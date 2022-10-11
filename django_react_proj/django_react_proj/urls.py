from django.contrib import admin
from django.urls import path, re_path
from teachers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/teachers/$', views.teachers_list),
    re_path(r'^api/teachers/([0-9])$', views.teachers_detail),
]