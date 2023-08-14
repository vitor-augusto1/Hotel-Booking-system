from enum import Enum, IntEnum
from uuid import UUID, uuid4

from pydantic import BaseModel


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
