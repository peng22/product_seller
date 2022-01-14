from django.urls import path, include
from .api_views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('auth_api', AuthViewSet, basename='auth_api')
router.register('products',ProductViewset)


urlpatterns = [
path("auth/", include("rest_framework.urls")),
path('user_list',UserList.as_view(),name="user_list"),
]

urlpatterns += router.urls
