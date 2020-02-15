import pytest


def test_root_available(client, settings):
    # The Django welcome page is only shown if DEBUG = True
    settings.DEBUG = True

    response = client.get("/")
    assert response.status_code == 200
