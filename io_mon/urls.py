from django.urls import include, path
from rest_framework import routers

from ios import views

router = routers.DefaultRouter()
router.register(r"inputs", views.InputViewSet)
router.register(r"outputs", views.OutputViewSet)
router.register(r"requests", views.RequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
