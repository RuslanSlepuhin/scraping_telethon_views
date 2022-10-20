from django.urls import path, include
from rest_framework import routers

from parser.views import MexView, LastSessionView, AdminLastSessionView

router = routers.DefaultRouter()
router.register('last-session', AdminLastSessionView, basename='last_session')

#
urlpatterns = [
    path('', include(router.urls)),
]