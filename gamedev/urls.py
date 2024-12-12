from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .models import IndieGame
from .views import GameDevView

router = DefaultRouter()
router.register(r'IndieGame', GameDevView)

urlpatterns = [
    path('', include(router.urls))
]