from rest_framework.routers import DefaultRouter

from .views import CollectionViewSet

app_name = 'collection'

router = DefaultRouter()

router.register("", CollectionViewSet, basename='collection')

urlpatterns = router.urls
