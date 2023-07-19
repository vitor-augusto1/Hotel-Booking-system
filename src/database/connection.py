from typing import List, Optional
from uuid import UUID
from schemas.Room import Room
import sqlite3


class Database:
    def __init__(self) -> None:
        self.db_instance = sqlite3.connect("hotel_system.db", check_same_thread=False)
        self.cursor = self.db_instance.cursor()

    def create_rooms_table(self) -> None:
        query = f"""
        CREATE TABLE rooms (id text, room_status integer, room_type text, price real)
        """
        self.cursor.execute(query)
        self.db_instance.commit()
        print("Table successfully created")

    def create_new_room(self, room: Room) -> None:
        print(f"This is the room being created: {room}")
        query = f"""
        INSERT INTO rooms VALUES ('{room.id}', '{room.room_status}',
                           '{room.room_type.name}', '{room.price}')
        """
        self.cursor.execute(query)
        self.db_instance.commit()

    def return_all_rooms(self) -> Optional[List[Room]]:
        query = """
        SELECT * FROM rooms
        """
        rooms = self.cursor.execute(query).fetchall()
        return rooms

    def return_room_by_id(self, id: UUID) -> Optional[Room]:
        query = f"""
        SELECT * FROM rooms WHERE id = '{id}';
        """
        room = self.cursor.execute(query).fetchall()
        print(f"Founded room: {room}")
        return room


db: Database = Database()


if __name__ == "__main__":
    db.create_rooms_table()
