from django.urls import include, path
from rest_framework import routers

from ios import views

router = routers.DefaultRouter()
router.register(r'inputs', views.InputViewSet, basename='input')
router.register(r'outputs', views.OutputViewSet, basename='output')
router.register(r'requests', views.RequestViewSet,  basename='request')

urlpatterns = [
    path('', include(router.urls)),
]