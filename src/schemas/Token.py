import datetime
import uuid
from pydantic import BaseModel
from uuid import UUID


class TokenPayload(BaseModel):
    customer_id: str
    exp: datetime.datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=4)
