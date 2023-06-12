from typing import List
from pydantic import BaseModel


class Berry(BaseModel):
    name: str
    growth_time: int


class BerriesStatistics(BaseModel):
    berries_names: List[str] = []
    min_growth_time: str
    median_growth_time: str
    variance_growth_time: str
    mean_growth_time: str
    frequency_growth_time: dict
