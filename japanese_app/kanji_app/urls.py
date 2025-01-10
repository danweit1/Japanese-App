from django.urls import path
from .views import KanjiListView

urlpatterns = [
    path('', KanjiListView.as_view(), name='kanji_list'),
]
