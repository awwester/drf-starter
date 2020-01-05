from rest_framework import routers

from accounts.views import UserViewSet
from items.views import ItemViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'items', ItemViewSet)
