import pytest
from rest_framework.test import APIClient

MENU_ITEMS_API_URL = "/api/v1/menu_items/"


@pytest.mark.django_db()
class TestMenuItemsView:
    def test_should_view_response_with_menu_items(
        self, client_with_credentials: APIClient
    ):
        response = client_with_credentials.get(MENU_ITEMS_API_URL)
