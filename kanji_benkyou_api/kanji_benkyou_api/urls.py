"""kanji_benkyou_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from kanjis import views as kanji_views
from quiz.urls import router as quiz_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('kanjis/search/', kanji_views.search_kanji), 
    path('romaji_to_kana/', kanji_views.romaji_to_kana),
    path('kanji_order/', kanji_views.kanji_order),
    path('kanji_by_jlpt/', kanji_views.kanji_by_jlpt),
    path('', include(quiz_router.urls)),
]
