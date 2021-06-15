from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('saloon', views.Saloon)

urlpatterns = [
    path('view/', include(router.urls)),
]
