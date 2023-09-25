
from fastapi import FastAPI
from services.connection.db import engine
from models.base import Base
from api.user import user
from api.admin import admin
from api.advisor import advisor
import uvicorn

app = FastAPI()

app.include_router(user.router)
app.include_router(admin.router)
app.include_router(advisor.router)

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
