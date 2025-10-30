from fastapi import FastAPI
from database import connect
from contextlib import asynccontextmanager
from routes import signuproute, usersroutes, productsroute, supplierroute


@asynccontextmanager
async def lifespan(app:FastAPI):
    connect()
    yield

app = FastAPI(
    title="Inventory",
    version="0.1.1",
    lifespan=lifespan
)

app.include_router(signuproute.routes)
app.include_router(usersroutes.routes)
app.include_router(productsroute.routes)
app.include_router(supplierroute.routes)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)