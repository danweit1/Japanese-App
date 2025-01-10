"""
URL configuration for japanese_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from kanji_app.views import KanjiListView
from grammar.views import GrammarListView
from vocab.views import VocabListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/kanji/', KanjiListView.as_view(), name='kanji_list'),
    path('api/grammar/', GrammarListView.as_view(), name='grammar_list'),
    path('api/vocab/', VocabListView.as_view(), name='vocab_list'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

