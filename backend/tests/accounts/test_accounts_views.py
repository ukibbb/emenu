import json
from http.client import CREATED

import pytest
from accounts.views import UserRegisterView
from rest_framework import status
from rest_framework.test import APIRequestFactory

REGISTER_API_URL = "/api/v1/accounts/register/"
MY_ACCOUNT_API_URL = "/api/v1/accounts/me/"


@pytest.mark.django_db(transaction=False)
class TestUsersApiView:
    def test_user_register_view(
        self, request_factory: APIRequestFactory, user_data: dict
    ) -> None:
        data = {
            "email": user_data.get("email"),
            "password": user_data.get("password"),
        }

        request = request_factory.post(
            REGISTER_API_URL, json.dumps(data), content_type="application/json"
        )

        response = UserRegisterView.as_view()(request)
        assert response.status_code == CREATED

    def test_user_register_view_without_email(
        self, request_factory: APIRequestFactory, user_data: dict
    ) -> None:
        data = {
            "email": "nomail",
            "password": user_data.get("password"),
        }

        request = request_factory.post(
            REGISTER_API_URL, json.dumps(data), content_type="application/json"
        )

        response = UserRegisterView.as_view()(request)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
