from app import health_check, get_environment


def test_health_check():
    assert health_check() == "OK"


def test_environment():
    assert get_environment() == "production"
