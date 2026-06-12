from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app):

    print("Application Starting...")

    yield

    print("Application Shutting Down...")