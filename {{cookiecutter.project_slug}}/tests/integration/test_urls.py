import pytest


def test_root_available(client, settings):
    response = client.get("/")
    assert response.status_code == 200
