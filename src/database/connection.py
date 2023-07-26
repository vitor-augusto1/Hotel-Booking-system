import select
from typing import List, Optional
from uuid import UUID
from schemas.Room import Room, RoomType
from schemas.Customer import Customer
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

    def return_all_available_rooms(self) -> Optional[List[Room]]:
        query = """
        SELECT * FROM rooms WHERE room_status = 0;
        """
        rooms: Optional[List[Room]] = self.cursor.execute(query).fetchall()
        return rooms

    def return_all_available_rooms_by_its_type(
            self, room_type: RoomType) -> Optional[List[Room]]:
        query = f"""
        SELECT * FROM rooms WHERE room_status = 0 AND room_type = '{room_type}'
        """
        rooms: Optional[List[Room]] = self.cursor.execute(query).fetchall()
        print(f"Rooms founded: {rooms}")
        return rooms

    def return_rooms_by_price_range(
            self, min_price: float, max_price: float) -> Optional[List[Room]]:
        query = f"""
        SELECT * FROM rooms WHERE price >= {min_price} AND price <= {max_price}
        """
        rooms: Optional[List[Room]] = self.cursor.execute(query).fetchall()
        return rooms

    def return_all_available_rooms_by_price_range(
            self, min_price: float, max_price: float) -> Optional[List[Room]]:
        query = f"""
        SELECT * FROM rooms WHERE price >= {min_price} \
        AND price <= {max_price} AND room_status = 0;
        """
        rooms: Optional[List[Room]] = self.cursor.execute(query).fetchall()
        return rooms

    def return_available_rooms_by_price_range_and_type(
            self, min_price: float, max_price: float,
            room_type: RoomType) -> Optional[List[Room]]:
        print(f"Room that user wants: mip = {min_price}, mxp = {max_price}, tp = {room_type}")
        query = f"""
        SELECT * FROM rooms WHERE price >= {min_price} AND \
        price <= {max_price} AND room_type = '{room_type}' AND room_status = 0;
        """
        rooms: Optional[List[Room]] = self.cursor.execute(query).fetchall()
        return rooms

    def create_customers_table(self) -> None:
        drop_table_query = f"""
        DROP TABLE customers;
        """
        query = """
        CREATE TABLE customers (id text, first_name text, middle_name text, \
                last_name text, password text, booking_id text)
        """
        self.cursor.execute(drop_table_query)
        self.cursor.execute(query)
        self.db_instance.commit()
        print("Table 'customers' successfully created")

    def create_new_customer(self, customer: Customer) -> None:
        print(f"This is the customer being created: {customer}")
        print(f"Pass:  {customer.password.decode()}")
        query = f"""
        INSERT INTO customers VALUES ('{customer.id}', '{customer.first_name}', '{customer.middle_name}', '{customer.last_name}', '{customer.password.decode()}', '{customer.booking_id}');
        """
        print(f"This is the query: {query}")
        self.cursor.execute(query)
        self.db_instance.commit()


db: Database = Database()


if __name__ == "__main__":
    db.create_rooms_table()
