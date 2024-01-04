# In your Django project's urls.py
from django.urls import path
from mock_api.views import ClickUpSpacesView
from .views import ClickUpDataListCreateView

urlpatterns = [
    path('clickup-spaces/', ClickUpSpacesView.as_view(), name='clickup-spaces'),
    path('clickup-data/', ClickUpDataListCreateView.as_view(), name='clickup-data-list-create'),
]
