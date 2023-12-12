import shutil
from typing import List
from uuid import uuid4

from fastapi import FastAPI, UploadFile, File

from UserModel import User

app = FastAPI()

# import sqlite3
#
# con = sqlite3.connect("postappdb.db")
# cursor = con.cursor()
# cursor.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT)")

db: List[User] = [

]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/users")
async def get_users():
    return db


@app.post("/users")
async def send_users(user: User):


    db.append(user)
    return {"OK"}


@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
   with open("destination.png", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
   return {"filename": file.filename}
