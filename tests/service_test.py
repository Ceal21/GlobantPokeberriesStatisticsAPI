from src import service


def test_get_berries_count():
    assert service.get_berries_count() >= 0


def test_get_all_berry_urls():
    assert len(service.get_all_berry_urls(100)) > 0


def test_get_berries():
    assert len(service.get_berries()) > 0
