from typing import Dict

from fastapi import FastAPI, responses

from src.models import BerriesStatistics
from src.service import get_berries_statistics

app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    """ Return the SWAGGER documentation """
    return responses.RedirectResponse('/docs')


@app.get("/allBerryStats/")
async def all_berry_stats() -> BerriesStatistics:
    """
    Return a Dictionary with a resume of all the existing Pokeberries
    """
    return get_berries_statistics()


@app.get("/healthcheck/", include_in_schema=False)
async def healthcheck() -> Dict[str, str]:
    """
    Return ok if the server is up
    """
    return {"status": "ok"}
