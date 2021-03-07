from fastapi import FastAPI

from cars_api import models
from cars_api.database import engine
from cars_api.routers.dealers import router as dealers_router
from cars_api.routers.vehicles import router as vehicles_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(dealers_router, prefix="/dealers", tags=["dealers"])
app.include_router(vehicles_router, prefix="/vehicles", tags=["vehicles"])
