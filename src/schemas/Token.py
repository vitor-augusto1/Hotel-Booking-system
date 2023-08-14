import datetime
import uuid
from uuid import UUID

from pydantic import BaseModel


class TokenPayload(BaseModel):
    customer_id: str
    exp: datetime.datetime = datetime.datetime.utcnow() + datetime.timedelta(
        hours=4
    )
    is_admin: bool
