from django.contrib import admin
from django.urls import path, re_path, include
from teachers.views import TeacherViewSet
from rest_framework import routers


class MyCustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}$',
                    mapping={'get': 'list'},
                    name='{basename}-list',
                    detail=False,
                    initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                    mapping={'get': 'retrieve'},
                    name='{basename}-detail',
                    detail=True,
                    initkwargs={'suffix': 'Detail'})
    ]

router = MyCustomRouter()
router.register(r'teachers', TeacherViewSet, basename='teachers')
print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]