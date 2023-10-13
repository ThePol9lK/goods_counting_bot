import uvicorn
from fastapi import FastAPI
from database import SessionLocal, engine, Base
from routers import user as UserRouter
from routers import category as CategoryRouter
from routers import product as ProductRouter
from routers import transaction as TransactionRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(UserRouter.router, prefix='/user')
app.include_router(CategoryRouter.router, prefix='/category')
app.include_router(ProductRouter.router, prefix='/product')
app.include_router(TransactionRouter.router, prefix='/transaction')

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True, workers=3)
