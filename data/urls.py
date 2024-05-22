from django.urls import path
from .views import fetch_and_store_data

urlpatterns = [
    path('fetch-data/', fetch_and_store_data, name='fetch_data'),
]
