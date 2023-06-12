import httpx

from typing import List


def get_data_from_url(url: str) -> dict:
    """ Return a JSON after a HTTPX request 200 code. """
    try:
        r = httpx.get(url)

        if r.status_code == 200:
            return r.json()
    except httpx.HTTPError as exc:
        print(f"HTTP Exception for {exc.request.url} - {exc}")


def get_mean(numbers: List[int]) -> float:
    """ Return the mean of a number list """
    return sum(numbers) / len(numbers) if numbers else 0


def get_variance(numbers: List[int]) -> float:
    """ Return the variance of a number list """
    return (
        sum((i - get_mean(numbers)) ** 2 for i in numbers)
        / len(numbers)
    ) if numbers else 0
