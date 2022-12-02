from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import *

app_name = 'blog'

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = router.urls
