from fastapi import FastAPI
from routes.tasks import router
from utils.database import init_db


app = FastAPI()

init_db()

app.include_router(router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)