from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('register', views.RegisterView)

urlpatterns = [
    path('account/', include(router.urls)),
    path('account/logout/', views.LogoutView.as_view()),
    path('account/login/refresh', TokenRefreshView.as_view()),
    path('account/login/', TokenObtainPairView.as_view()),
]

