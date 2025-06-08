from rest_framework.routers import DefaultRouter
from .views import SerieViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'series', SerieViewSet)
router.register(r'categories', CategoriaViewSet)

urlpatterns = router.urls
