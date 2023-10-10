from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello"}

@app.get("/profile")
def get_root():
    return {"name": "Hans","email": "hans@wurst.de"}


handler = Mangum(app)