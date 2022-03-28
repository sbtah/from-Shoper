import pytest
from mixer.backend.django import mixer
from products.models import Product


pytestmark = pytest.mark.django_db
