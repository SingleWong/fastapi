# -*- coding: utf-8 -*-

from app import create_app
from fastapi.middleware.cors import CORSMiddleware


app = create_app()

# origins = [
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=['*'],
    # allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/health')
async def health_api():
    return "Health"
