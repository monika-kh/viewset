from django.conf.urls import url
from rest_framework import routers

from std.views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register(r"students", StudentViewSet, basename="students")
router.register(r"universities", UniversityViewSet, basename="universities")


urlpatterns = router.urls
