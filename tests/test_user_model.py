import pytest
from django.contrib.auth import get_user_model


pytestmark = pytest.mark.django_db


class TestUserModel:
    """Test cases for User object."""

    def test_create_user_with_email_succesful(self):
        """Test creating new user with email."""

        assert get_user_model().objects.all().count() == 0
        email = "test@test.com"
        password = "testpass123!"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        assert user.email == "test@test.com"
        assert user.check_password(password) == True

    def test_new_user_email_normalized(self):
        """Test that email for new user is normalized."""

        email = "test@TEST.com"
        password = "testpass123!"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        assert user.email == email.lower()

    def test_new_user_with_invalid_email(self):
        """Test creating user with no email raises an error."""

        with pytest.raises(Exception) as error:
            get_user_model().objects.create_user("", "test123!")

    def test_create_super_user(self):
        """Test creating new super user."""

        assert get_user_model().objects.filter(is_superuser=True).exists() == False
        email = "admin@admin.com"
        password = "testpass123!"
        user = get_user_model().objects.create_superuser(
            email=email,
            password=password,
        )
        assert user.is_superuser == True
        assert user.is_staff == True

    def test_create_user_with_email_already_used(self):
        """Test that creation user with used email raises an exception."""

        user_1 = get_user_model().objects.create_user(
            email="test@test.com",
            password="testpass123",
        )
        with pytest.raises(Exception) as error:
            get_user_model().objects.create_user(
                email="test@test.com",
                password="testpass123",
            )
