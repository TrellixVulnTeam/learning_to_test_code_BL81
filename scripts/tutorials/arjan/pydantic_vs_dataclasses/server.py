# server.py

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/api/home/{s}")
def homepage(s: int):
    return {"message": s * s}

@app.get("/api/int/{i}")
def endpoint(i: int):
    return {"i" : i}

if __name__ == "__main__":
    uvicorn.run(app)