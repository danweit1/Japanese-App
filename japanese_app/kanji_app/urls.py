from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KanjiViewSet

router = DefaultRouter()
router.register(r'kanji', KanjiViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
]
