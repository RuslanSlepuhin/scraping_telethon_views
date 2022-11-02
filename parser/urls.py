from django.urls import path, include
from rest_framework import routers

from parser.views import MexView, AdminLastSessionView, GetFromAdminView, PatternView, BackendView, PatternChangeView

router = routers.DefaultRouter()
router2 = routers.SimpleRouter()
router.register('last-session', AdminLastSessionView, basename='last_session')
router2.register('backend', BackendView, basename='pattern')
router.register('pattern_modify', PatternChangeView, basename='modify')
#
urlpatterns = [
    path('', include(router.urls)),
    path('', include((router2.urls))),
    path('post-approved', GetFromAdminView.as_view()),
    path('pattern', PatternView.as_view()),

]