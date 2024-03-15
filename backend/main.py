import json

from fastapi import FastAPI
from api import router
from manticore_utils import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
        "https://physicsmathcode.aboba.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    with open("./messages.json", "r") as messages_file:
        posts = json.loads(messages_file.read())
        assert init_db(posts)


app.include_router(router, prefix="/api", tags=["API physics.math.code"])
