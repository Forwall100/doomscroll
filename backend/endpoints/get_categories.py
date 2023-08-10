from fastapi import APIRouter, Query, HTTPException
from utils.adapter import FeedAdapter
from utils.constans import FEED_PATH
import feedparser
from newspaper import Article
from random import randint

router = APIRouter()

@router.get("/get-categories")
async def get_post():
    adapter = FeedAdapter(FEED_PATH)
    try:
        return {"categories": adapter.get_categories()}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
