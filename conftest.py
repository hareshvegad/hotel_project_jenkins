import pytest
from django.conf import settings
from decouple import config
from rest_framework.test import APIClient
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotel_project.test_settings")
django.setup()

@pytest.fixture
def api_client():
    return APIClient()