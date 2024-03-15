import typing
from pprint import pprint

from fastapi import APIRouter

from pydantic_models.search import SearchQuery, SearchResponse
from manticore_utils.search import SearchPosts

router = APIRouter()


@router.post("/search", response_model=typing.List[SearchResponse])
async def search(body: SearchQuery):
    # pprint(SearchPosts.search(body.tolerance, body.query))
    return SearchPosts.search(body.tolerance, body.query)
