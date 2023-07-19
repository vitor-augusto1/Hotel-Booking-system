from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum, IntEnum


class RoomStatus(IntEnum):
    OCCUPIED = 1
    EMPTY = 0


class RoomType(IntEnum):
    BASIC = 1
    CLASSIC = 2
    LUXURY = 3


class Room(BaseModel):
    id: UUID = uuid4()
    room_status: RoomStatus
    room_type: RoomType
    price: float
