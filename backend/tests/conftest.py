import django
import pytest
from accounts.models import User
from menu_items.models import MenuItem
from menus.models import Menu
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework_simplejwt.tokens import AccessToken

django.setup()


@pytest.fixture
def authorization_header(user: User) -> dict:
    """Generate a token and return dictionary with authorization header
    that can be used in client requests."""
    token = AccessToken.for_user(user)
    return {"HTTP_AUTHORIZATION": f"Bearer {str(token)}"}


@pytest.fixture
def client() -> APIClient:
    """Create a new APIClient, so we are sure that sessions and cookies are not shared between tests."""
    return APIClient()


@pytest.fixture
def client_with_credentials(client: APIClient, authorization_header: dict) -> APIClient:
    """Created client with login credentials passed."""
    client.credentials(**authorization_header)
    return client


@pytest.fixture
def request_factory() -> APIRequestFactory:
    """Helper fixture for requests."""
    return APIRequestFactory()


@pytest.fixture(scope="module")  # run once per test module.
def user_data() -> dict:
    return {
        "id": "1f124eb0-cf7b-405b-8f0f-1f00ee2aed35",
        "email": "John.Doe@example.com",
        "password": "passJohn1",
    }


@pytest.fixture
def superuser(user_data) -> User:
    superuser, _ = User.objects.get_or_create(
        email=user_data["email"], is_staff=True, is_active=True, is_superuser=True
    )
    return superuser


@pytest.fixture
def menus_data() -> dict:
    return {"name": "Greek", "description": "Menu with food from greece."}


@pytest.fixture
def menu(menus_data):
    return Menu.objects.create(
        name=menus_data["name"], description=menus_data["description"]
    )


@pytest.fixture
def menu_items_data() -> dict:
    return {
        "name": "Gyros",
        "description": "Tasty meat",
        "price": 20.0,
        "is_vegetarian": True,
        "preparation_time": "00:30:00",
    }


@pytest.fixture
def user(user_data) -> User:
    user = User.objects.create(
        password=user_data["password"],
        email=user_data["email"],
        is_staff=False,
        is_active=True,
        is_superuser=False,
    )
    return user


@pytest.fixture
def menus(menus_data, menu_items) -> list[Menu]:
    return [
        Menu.objects.create(
            name=menu["name"], description=menu["description"], items=menu_items
        )
        for menu in menus_data
    ]


@pytest.fixture
def menu_items(menu_items_data) -> list[MenuItem]:
    return [
        MenuItem.objects.create(
            name=menu_item["name"],
            description=menu_item["description"],
            price=menu_item["price"],
            preparation_time=menu_item["preparation_time"],
            is_vegetarian=menu_item["is_vegetarian"],
        )
        for menu_item in menu_items_data
    ]
