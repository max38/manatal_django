from django.urls import path, include
from rest_framework_nested import routers
from .views import SchoolViewSet, StudentNestedViewSet, StudentViewSet

app_name = 'school'

router = routers.SimpleRouter()
router.register(r'schools', SchoolViewSet)

schools_router = routers.NestedSimpleRouter(router, r'schools', lookup='school')
schools_router.register(r'students', StudentNestedViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include(schools_router.urls)),
    path('students/', StudentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='students'),
    path('students/<str:pk>', StudentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='student-detail'),
]
