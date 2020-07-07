from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from .views import VowelCountView, HistoryViewSet

router = SimpleRouter()
router.register("history", HistoryViewSet, basename='history')

urlpatterns = router.urls + [
    url(r'^vowelcount', VowelCountView.as_view(), name='vowelcount')]
