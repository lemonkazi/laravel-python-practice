from fastapi import FastAPI
from .api import api_router

app = FastAPI(
    title="News Aggregator API",
    version="1.0.0"
)

# Include API routes
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the News Aggregator API"}

