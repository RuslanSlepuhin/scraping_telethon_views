from django.urls import path, include
from rest_framework import routers

from parser.views import MexView, AdminLastSessionView, GetFromAdminView, PatternView

router = routers.DefaultRouter()
router.register('last-session', AdminLastSessionView, basename='last_session')
# router.register('pattern', PatternView, basename='pattern')
#
urlpatterns = [
    path('', include(router.urls)),
    path('post-approved', GetFromAdminView.as_view()),
    path('pattern', PatternView.as_view()),
]