from home.viewsets import HomeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('home',HomeViewset)