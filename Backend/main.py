from fastapi import FastAPI
from database import connect
from contextlib import asynccontextmanager
from routes import (
    signuproute, 
    usersroutes, 
    productsroute, 
    supplierroute, 
    categoryroute, 
    category_images,
    salesroutes,
    purchaseroutes,
    stockmovementroutes,
    warehouseroute,
    )


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
app.include_router(categoryroute.routes)
app.include_router(category_images.routes)
app.include_router(salesroutes.routes)
app.include_router(purchaseroutes.routes)
app.include_router(stockmovementroutes.routes)
app.include_router(warehouseroute.routes)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)