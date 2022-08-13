import pytest
from mixer.backend.django import mixer
from images.models import Image


pytestmark = pytest.mark.django_db


class TestImageObject:
    """Test cases for Image object."""

    def test_image_can_be_created(self):
        """Test that image object is created and saved to db."""

        assert Image.objects.count() == 0
        image = mixer.blend(Image)
        assert Image.objects.count() == 1

    def test_str_method_of_image(self):
        """Test that __str__ is properly generated."""

        image = mixer.blend(Image, shoper_gfx_id="007", shoper_product_id="999")
        assert (
            str(image)
            == f"GFX-ID:{image.shoper_gfx_id} Product-ID:{image.shoper_product_id}"
        )
