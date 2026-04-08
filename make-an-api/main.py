from fastapi import FastAPI, HTTPException
import random
import string

app = FastAPI()
data = {}


@app.post("/ip/{ip}")
def create_code(ip: str):
    code = "".join(random.choices(string.ascii_lowercase, k=5))

    data[code] = ip
    return {"code": code, "ip": ip}


@app.get("/code/{code}")
def get_ip(code: str):
    if code not in data:
        raise HTTPException(status_code=404, detail="Code not found")
    return {"ip": data.get(code, "Not found")}
