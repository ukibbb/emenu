import pytest
from accounts.serializers import UserRegistrationSerializer, UserSerializer


@pytest.fixture()
def users_key():
    return ["email"]


@pytest.fixture()
def users_registration_key():
    return ["id", "email", "password"]


@pytest.mark.django_db(transaction=False)
def test_user_should_be_serialized(user, users_key, user_data):
    serializer = UserSerializer(instance=user)
    data = serializer.data
    assert set(data.keys()) == set(users_key)
    for key in users_key:
        assert data[key] == user_data[key]


@pytest.mark.django_db(transaction=False)
def test_user_during_registration_should_be_serialized(
    user, users_registration_key, user_data
):
    serializer = UserRegistrationSerializer(instance=user)
    data = serializer.data
    assert set(data.keys()) == set(users_registration_key)
    assert all(
        data[key] == user_data[key] for key in users_registration_key if key != "id"
    )
