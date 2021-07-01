from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('saloon', views.SaloonView)
router.register('saloon/edit', views.SaloonEdit)

urlpatterns = [
    path('view/', include(router.urls)),
]

