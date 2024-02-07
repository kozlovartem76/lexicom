from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from redis import StrictRedis


app = FastAPI()
redis_client = StrictRedis(host="redis", port=6379, decode_responses=True)


class Data(BaseModel):
    phone: str
    address: str


@app.post("/write_data")
async def write_data(data: Data):

    redis_client.hset("addresses", data.phone, data.address)

    return {"message": "Data written successfully"}


@app.put("/write_data")
async def update_data(data: Data):

    if not redis_client.hexists("addresses", data.phone):
        raise HTTPException(status_code=404, detail="Phone not found")

    redis_client.hset("addresses", data.phone, data.address)

    return {"message": "Data updated successfully"}


@app.get("/check_data")
async def check_data(phone: str):

    address = redis_client.hget("addresses", phone)

    if not address:
        raise HTTPException(status_code=404, detail="Phone not found")
    return {"phone": phone, "address": address}
