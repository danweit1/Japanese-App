from django.urls import path
from .views import GrammarListView

urlpatterns = [
    path('', GrammarListView.as_view(), name='grammar_list'),
]
