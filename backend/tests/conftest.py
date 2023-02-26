import django
import pytest
from accounts.models import User
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework_simplejwt.tokens import AccessToken

django.setup()


@pytest.fixture
def authorization_header(user: User) -> dict:
    """Generate a toke and return dictionary with authorization header
    that can be used in client requests."""
    token = AccessToken.for_user(user)
    return {"HTTP_AUTHORIZATION": f"Bearer {str(token)}"}


@pytest.fixture
def client() -> APIClient:
    """Create a new APIClient, so we are sure that sessions and cookies are not shared between tests."""
    return APIClient()


@pytest.fixture
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture(scope="module")  # run once per test module.
def user_data():
    return {
        "id": "1f124eb0-cf7b-405b-8f0f-1f00ee2aed35",
        "email": "John.Doe@example.com",
        "password": "passJohn1",
    }


@pytest.fixture()
def superuser(user_data):
    superuser, _ = User.objects.get_or_create(
        email=user_data["email"], is_staff=True, is_active=True, is_superuser=True
    )
    return superuser


@pytest.fixture()
def user(user_data):
    user, _ = User.objects.get_or_create(
        password=user_data["password"],
        email=user_data["email"],
        is_staff=False,
        is_active=True,
        is_superuser=False,
    )
    return user
