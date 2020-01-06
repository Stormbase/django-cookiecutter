import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_admin_superuser():
    User.objects.create_superuser("admin", email="admin@example.com", password="secret")

    admin = User.objects.get(username="admin")
    assert admin.is_superuser
