from rest_framework import routers

from accounts.views import UserViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
