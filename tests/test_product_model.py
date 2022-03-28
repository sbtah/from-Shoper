import pytest
from mixer.backend.django import mixer
from products.models import Product
from images.models import Image


pytestmark = pytest.mark.django_db


class TestProductObject:
    """Test cases for Product model."""

    def test_product_can_be_created(self):
        """Test that product object is created and saved to db."""

        assert Product.objects.all().count() == 0
        product = mixer.blend(Product)
        assert Product.objects.all().count() == 1

    def test_str_method_of_product(self):
        """Test that __str__ is properly generated."""

        product = mixer.blend(
            Product, shoper_title_pl="Test product", shoper_id="007", shopify_id="008"
        )
        assert (
            str(product)
            == f"{product.shoper_title_pl} ShoperID:{product.shoper_id} ShopifyID:{product.shopify_id}"
        )

    def test_save_method_of_product(self):
        """Test that proper image is added to images field on model save."""

        image_1 = mixer.blend(Image, shoper_product_id="007")
        image_2 = mixer.blend(Image, shoper_product_id="007")
        image_3 = mixer.blend(Image, shoper_product_id="008")
        product = mixer.blend(Product, shoper_id="007")
        assert image_1 in product.images.all()
        assert image_2 in product.images.all()
        assert image_3 not in product.images.all()

    def test_signal_for_product(self):
        """Test that image_added_removed_product method on Product model properly update Image's fields."""

        image_1 = mixer.blend(Image)
        image_1.save()
        product = mixer.blend(Product, shoper_id="007")
        assert image_1 not in product.images.all()
        product.images.add(image_1)
        image_1.refresh_from_db()
        assert image_1 in product.images.all()
        assert image_1.shoper_product_id == "007"
        product.images.remove(image_1)
        image_1.refresh_from_db()
        assert image_1 not in product.images.all()
        assert image_1.shoper_product_id == ""
        assert image_1.order == ""
        assert image_1.shoper_main == False
        assert image_1.shoper_unic == ""
