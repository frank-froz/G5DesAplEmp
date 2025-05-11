from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
