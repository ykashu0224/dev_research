from rest_framework.routers import DefaultRouter
from . import views

app_name = "hello"
router = DefaultRouter()
router.register("", views.HelloViewSet)


urlpatterns = router.urls