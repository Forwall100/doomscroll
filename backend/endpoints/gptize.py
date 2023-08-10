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
Please provide a sammarie of the article below in the following format - 
First, briefly summarize what the article is about and write the main point of the article
Next, choose the top 5 points from the article and write them.
The sammari should be divided into paragraphs and at the beginning of each paragraph there should be an emoji that fits the meaning.
The received sammarie should be at least 1000 characters in size and should be submitted in Russian.
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
