from django.urls import path
from .views import VocabListView

urlpatterns = [
    path('', VocabListView.as_view(), name='vocab_list'),
]
