import pytest
from accounts.models import User
from menus.views import MenuViewSet
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate

MENUS_API_URL = "/api/v1/menus/"


@pytest.mark.django_db()
class TestMenusView:
    def test_should_view_be_protected_without_token(self, client: APIClient) -> None:
        response = client.get(MENUS_API_URL)
        assert response.status_code == HTTP_401_UNAUTHORIZED

    def test_should_view_be_protected(
        self, request_factory: APIRequestFactory, user: User
    ) -> None:
        request = request_factory.get(MENUS_API_URL)
        force_authenticate(request, user=user)
        response = MenuViewSet.as_view({"get": "list"})(request)
        assert response.status_code == HTTP_200_OK

    def test_should_view_be_protectede_with_token(
        self, client: APIClient, authorization_header: dict
    ):
        client.credentials(**authorization_header)
        response = client.get(MENUS_API_URL)
        assert response.status_code == HTTP_200_OK

    def test_should_return_menus_with_items_only(
        self, client_with_credentials: APIClient
    ):
        response = client_with_credentials.get(MENUS_API_URL)
        assert len(response.data) == 2
