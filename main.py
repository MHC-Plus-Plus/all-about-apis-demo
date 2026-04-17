from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import random
import string

app = FastAPI()
data = {}


class IPRequest(BaseModel):
    ip: str


@app.get("/")
def health():
    """returns true. used to see if a server is running"""
    return True


@app.post("/host", status_code=status.HTTP_201_CREATED)
def host_game(body: IPRequest):
    code = "".join(random.choices(string.ascii_uppercase, k=5))

    data[code] = body.ip
    print(data)
    return {"code": code, "ip": body.ip}


@app.put("/{code}/host")
def update_game(code: str, body: IPRequest):
    data[code] = body.ip
    return {"ip": body.ip, "code": code}


@app.get("/{code}/join")
def join_game(code: str):
    if not code in data.keys():
        return HTTPException(404)
    ip = data[code]
    print(f"user joined game {code} @ {ip}")
    return {"ip": ip, "code": code}


@app.delete("/{code}/delete")
def close_game(code: str):
    data.pop(code)
