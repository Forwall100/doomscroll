from fastapi import FastAPI
import uvicorn
from endpoints import post
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

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=PORT,
        host=HOST,
        reload=True
    )