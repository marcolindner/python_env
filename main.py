from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello"}


handler = Mangum(app)