from src import utils

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_mean_empty_list():
    assert utils.get_mean([]) == 0


def test_mean_valid_list():
    assert utils.get_mean(NUMBERS) == 4.5


def test_get_variance_empty_list():
    assert utils.get_variance([]) == 0


def test_get_variance_valid_list():
    assert utils.get_variance(NUMBERS) == 8.25


def test_get_data_from_wrong_url():
    assert utils.get_data_from_url('asdasdas') is None


def test_get_data_from_url():
    url = 'https://pokeapi.co/api/v2/berry/'
    assert type(utils.get_data_from_url(url)) == dict
