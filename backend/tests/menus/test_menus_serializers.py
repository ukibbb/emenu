import pytest
from menus.serializers import MenuSerializer
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


@pytest.fixture()
def menus_key():
    return ["name", "description", "items", "created_at", "updated_at", "url"]


@pytest.mark.django_db
def test_menu_should_be_serialized(menu, menus_key):
    factory = APIRequestFactory()
    request = factory.get("/api/v1/")
    context = {"request": Request(request)}
    serializer = MenuSerializer(instance=menu, context=context)
    data = serializer.data
    assert set(data.keys()) == set(menus_key)
