from fastapi import FastAPI

from models import Idx, Item, ResponseItem, Qry
from index import Index

app = FastAPI()


@app.post("/idx")
def create_index(index: Idx):
    Index.create_index(index.dict())


@app.post("/qry/{index_name}")
def query_index(index_name: str, query: Qry):
    idx = Index(index_name)
    return idx.query_item(query.dict())


@app.put("/item/{index_name}", response_model=ResponseItem)
def index_item(index_name: str, item: Item):
    idx = Index(index_name)
    embedding = idx.set_item(item.dict())
    return {"item": item, "embedding": embedding}


@app.delete("/item/{index_name}/{item_id}")
def delete_item(index_name: str, item_id: str):
    idx = Index(index_name)
    idx.remove_item(item_id)
    return {}
