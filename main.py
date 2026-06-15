from fastapi import FastAPI

from fastapi import HTTPException

from routers.books import router as books_router
from routers.search import router as search_router
from routers.stats import router as stats_router
from routers.filters import router as filters_router
from routers.users import router as users_router

from middleware.request_logger import log_requests
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from fastapi.middleware.gzip import GZipMiddleware

from starlette.middleware.trustedhost import TrustedHostMiddleware

from core.lifespan import lifespan

from exceptions.handlers import (
    http_exception_handler,
    validation_exception_handler,
    generic_exception_handler
)

app = FastAPI(
    title="Book Management API",
    lifespan=lifespan
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler
)

app.add_exception_handler(
    Exception,
    generic_exception_handler
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "127.0.0.1",
        "localhost",
        "testserver",
        "fastapi-learning-hjb1.onrender.com"
    ]
)

app.add_middleware(
    GZipMiddleware,
    minimum_size=1000
)

# Register Middleware
app.middleware("http")(log_requests)


@app.get("/", tags=["Welcome Note"])
def home():
    return {
        "message": "Welcome to the Book Management API! Explore the endpoints to manage and query your book collection."
    }


app.include_router(books_router)
app.include_router(search_router)
app.include_router(stats_router)
app.include_router(filters_router)
app.include_router(users_router)