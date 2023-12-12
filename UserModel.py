import datetime
from typing import Optional
from uuid import UUID, uuid4

from fastapi import UploadFile, File
from pydantic import BaseModel


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    email: str

