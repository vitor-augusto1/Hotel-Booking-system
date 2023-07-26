from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4


class Customer(BaseModel):
    id: UUID = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    booking_id: UUID
