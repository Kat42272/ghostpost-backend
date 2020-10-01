from django.urls import path, include
from rest_framework import routers
from ghostpost_api import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

