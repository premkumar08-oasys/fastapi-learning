from fastapi import FastAPI

from routers.books import router as books_router
from routers.search import router as search_router
from routers.stats import router as stats_router
from routers.filters import router as filters_router

app = FastAPI(
    title="Book Management API"
)

@app.get("/", tags=["Welcome Note"])
def home():
    return {
        "message": "Welcome to the Book Management API! Explore the endpoints to manage and query your book collection."
    }

app.include_router(books_router)
app.include_router(search_router)
app.include_router(stats_router)
app.include_router(filters_router)