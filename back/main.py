from fastapi import FastAPI
from routes.tasks import router
from utils.database import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

init_db()

app.include_router(router)

origins = [
       "http://localhost:4200",
   ]
app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)