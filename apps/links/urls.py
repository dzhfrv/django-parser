from rest_framework.routers import SimpleRouter

from .views import LinkResource

router = SimpleRouter()
router.register('links', LinkResource, basename='links')
urlpatterns = router.urls
