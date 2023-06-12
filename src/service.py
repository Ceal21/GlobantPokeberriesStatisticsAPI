import os
from statistics import median

from typing import List
from collections import Counter

from src.models import BerriesStatistics, Berry
from src.utils import get_data_from_url, get_mean, get_variance

BASE_URL = os.getenv('POKEAPI_URL', 'https://pokeapi.co/api/v2/')
BERRY_ENDPOINT = os.getenv('BERRY_ENDPOINT', 'berry')


def get_berries_count() -> int:
    """ Return the number of berries """
    data = get_data_from_url(f'{BASE_URL}{BERRY_ENDPOINT}/')
    return data.get('count', 0) if data else 0


def get_all_berry_urls(total_berries: int) -> List[str]:
    """ Return all berry URLs as JSON """
    data = get_data_from_url(
        f'{BASE_URL}{BERRY_ENDPOINT}/?limit={total_berries}'
    )

    return (
        [result['url'] for result in data.get('results')] if data
        else []
    )


def get_berries() -> List[Berry]:
    """ Return a list of Berries as objects. """
    total_berries = get_berries_count()
    berry_urls = get_all_berry_urls(total_berries)

    berries = []

    for url in berry_urls:
        berry = get_data_from_url(url)
        if berry:
            berries.append(
                Berry(
                    name=berry.get('name', 'unknown'),
                    growth_time=berry.get('growth_time', 0)
                )
            )

    return berries


def get_berries_statistics() -> BerriesStatistics:
    """ Return a BerriesStatistics object """
    berries = get_berries()

    berries_names = []
    growth_times = []

    for berry in berries:
        berries_names.append(berry.name)
        growth_times.append(berry.growth_time)

    # Sort the berries by name ASC
    berries_names.sort()

    # Calculate the statistics
    min_growth_time = min(growth_times) if growth_times else 0
    median_growth_time = median(growth_times) if growth_times else 0
    mean_growth_time = get_mean(growth_times)
    variance_growth_time = get_variance(growth_times)
    frequency_growth_time = Counter(growth_times)

    return BerriesStatistics(
        berries_names=berries_names,
        min_growth_time=str(min_growth_time),
        median_growth_time=str(median_growth_time),
        variance_growth_time=str(variance_growth_time),
        mean_growth_time=str(mean_growth_time),
        frequency_growth_time=frequency_growth_time
    )
