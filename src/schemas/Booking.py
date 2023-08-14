from datetime import date
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel


class Booking(BaseModel):
    id: UUID = uuid4()
    rooms: List[UUID]
    customer_id: UUID
    start_date: int
    end_date: int
