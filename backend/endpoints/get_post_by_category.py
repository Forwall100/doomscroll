from fastapi import APIRouter, Query, HTTPException
from utils.adapter import FeedAdapter
from utils.constans import FEED_PATH
import feedparser
from newspaper import Article
from random import randint

router = APIRouter()


@router.get("/post-by-category")
async def get_post_by_category(category: str):
    adapter = FeedAdapter(FEED_PATH)
    try:
        source_url, source_title = adapter.get_random_source_by_category(category)

        rss = feedparser.parse(source_url)

        url = rss['items'][randint(0, len(rss['items']))]['link']

        article = Article(url)
        article.download()
        article.parse()
        article.nlp()

        return {"source_title":source_title, "title": article.title, "summary": article.summary, "keywords": article.keywords, "link": url, "image": article.top_image}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

