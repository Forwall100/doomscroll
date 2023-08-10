from fastapi import FastAPI
import uvicorn
from endpoints import post, gptize, get_categories
from utils.constans import HOST, PORT
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(gptize.router)
app.include_router(get_categories.router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=PORT,
        host=HOST,
        reload=True
    )