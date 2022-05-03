from rest_framework.routers import DefaultRouter
from .MentalState.views import MentalStateViewSet
from .TherapyCenter.views import therapycenterViewSet
from .user.views import UserViewSet


router = DefaultRouter()

router.register(r'mentalhealthcarecenters', therapycenterViewSet, basename='mentalhealthcarecennters')
router.register(r'mentalstate', MentalStateViewSet, basename='mentalstate')
router.register(r'users', UserViewSet, basename= 'users')
