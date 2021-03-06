"""HeroForgeServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from HeroForgeApi.views.auth import login_user, register_user
from HeroForgeApi.views.classes import ClasssView
from HeroForgeApi.views.equipment import EquipmentView
from HeroForgeApi.views.featSet import FeatSetView
from HeroForgeApi.views.feats import FeatView
from HeroForgeApi.views.races import RaceView
from HeroForgeApi.views.skills import SkillView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'skills', SkillView, 'skill')
router.register(r'races', RaceView, 'race')
router.register(r'feats', FeatView, 'feat')
router.register(r'featSets', FeatSetView, 'featSet')
router.register(r'classes', ClasssView, 'classs')
router.register(r'equipment', EquipmentView, 'equipment')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
