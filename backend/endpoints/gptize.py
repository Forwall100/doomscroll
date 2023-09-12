from fastapi import APIRouter, Query, HTTPException
from utils.adapter import FeedAdapter
from utils.constans import FEED_PATH
import feedparser
from newspaper import Article
from random import randint
import g4f
from g4f.Provider import DeepAi


router = APIRouter()

summarize_prompt = """
Please, make this article into a post to the Telegram channel taking into account all my wishes: 
First, summarize the essence of the article and write the main idea of the article.
Next, choose a few most important points from the article and write them.
The post should be divided into paragraphs, and at the beginning of each paragraph there should be an emoji corresponding to the meaning.
The resulting post should be no more than 1500 characters in size and it should be written in Russian.
Article:\n
"""


@router.get("/gptize/")
async def gptize(article_url: str):
    adapter = FeedAdapter(FEED_PATH)
    try:
        article = Article(article_url)
        article.download()
        article.parse()
        article.nlp()
        print("Start gpt")
        summary = g4f.ChatCompletion.create(model='gpt-3.5-turbo', messages=[
            {"role": "user", "content": summarize_prompt+article.text}], stream=False, provider=DeepAi)
        print("STOP gpt")

        return {"title": article.title, "summary": summary, "keywords": article.keywords, "link": article_url, "image": article.top_image}
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
