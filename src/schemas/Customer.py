from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class Customer(BaseModel):
    id: UUID = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    email: str
    password: bytes
    booking_id: Optional[UUID]
