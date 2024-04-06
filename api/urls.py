from django.urls import path
from api.views import execute_tests

urlpatterns = [
    # Other URL patterns
    path('execute', execute_tests),
]
