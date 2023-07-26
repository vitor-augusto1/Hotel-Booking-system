from datetime import date
from typing import List
from pydantic import BaseModel
from uuid import UUID, uuid4


class Booking(BaseModel):
    id: UUID = uuid4()
    rooms: List[UUID]
    customer_id: UUID
    start_date: date
    end_date: date
