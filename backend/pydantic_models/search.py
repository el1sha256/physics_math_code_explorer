from typing import List

from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str
    tolerance: int


class SearchResponse(BaseModel):
    id: int
    media_name: str
    description: str = None

