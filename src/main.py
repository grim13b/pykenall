import json
from fastapi import FastAPI
from tinydb import TinyDB, Query
from tinydb.storages import MemoryStorage

app = FastAPI()
db = TinyDB(storage=MemoryStorage)

with open('./assets/ken_all.json', 'r') as f:
    ken_all_list = json.load(f)

db.insert_multiple(ken_all_list)


@app.get("/health")
def health_check():
    return "OK"


@app.get("/postalcode/{postal_code}")
def find_by_postalcode(postal_code: str):
    query = Query()
    return db.search(query.postalcode.matches(f'^{postal_code}'))


@app.get("/jiscode/{jis_code}")
def find_by_jiscode(jis_code: str):
    query = Query()
    return db.search(query.jisx0401x0402.matches(f'^{jis_code}'))
