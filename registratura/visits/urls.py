from django.urls import path
from rest_framework.routers import SimpleRouter
from visits.views import *

router = SimpleRouter()
router.register(r'visit', VisitViewSet)
router.register(r'doctor', DoctorViewSet)
router.register(r'device', DeviceViewSet)

urlpatterns = router.urls