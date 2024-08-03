from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from storage import Storage

app = FastAPI()
storage = Storage()


class Quote(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"I am": "Alive"}

@app.get("/quotes/")
def get_all_quotes():
    return storage.get_all_quotes()

@app.post("/quotes/")
def read_item(quote: Quote):
    storage.add_quote(quote.text)
    return quote

@app.get("/quotes/random/")
def get_random():
    quote = storage.get_random_quote()
    if quote:
        return {"quote": quote}
    else:
        raise HTTPException(status_code=404, detail="No quotes available")


