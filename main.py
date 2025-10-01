from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class WebhookData(BaseModel):
    contact_id: str
    name: str
    email: str

@app.get("/")
async def root():
    return {"message": "API funcionando 🚀"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/ghl-webhook")
async def receive_webhook(data: WebhookData):

    print(f"Webhook recibido: {data.dict()}")

    return {
        "status": "ok",
        "received": data.dict()
    }