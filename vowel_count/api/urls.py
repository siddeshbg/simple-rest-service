from django.conf.urls import url
from .views import vowel_count

urlpatterns = [
    url(r'^vowelcount', vowel_count, name="vowel_count"),
]