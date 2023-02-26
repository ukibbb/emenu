import pytest
from accounts.models import User


@pytest.mark.django_db()
class TestUsersModelsCase:
    """Standard User Test Case."""

    def test_user_should_be_saved(self, user: User) -> None:
        assert str(user) == f"{user.id} - {user.email}"
        assert user.is_superuser is False
        assert user.is_active is True
        assert user.is_staff is False

    def test_superuser_should_be_saved(self, superuser: User) -> None:
        assert superuser.is_superuser is True
        assert superuser.is_active is True
        assert superuser.is_staff is True
