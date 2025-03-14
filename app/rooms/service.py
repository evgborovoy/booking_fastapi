from datetime import date

from sqlalchemy import and_, func, or_, select

from app.bookings.models import Bookings
from app.services.base_dao import BaseDAO
from app.database import async_session_maker
from app.rooms.models import Rooms


class RoomDAO(BaseDAO):
    model = Rooms

    @classmethod
    async def find_all(cls, hotel_id: int, date_from: date, date_to: date):
        booked_rooms = (
            select(Bookings.room_id, func.count(Bookings.room_id).label("rooms_booked"))
            .select_from(Bookings)
            .where(
                and_(
                    date_from <= Bookings.date_to,
                    date_to >= Bookings.date_from
                )
            )
            .group_by(Bookings.room_id)
        ).cte("booked_rooms")

        get_rooms = (
            select(
                Rooms.__table__.columns,
                (Rooms.price * (date_to - date_from).days).label("total_cost"),
                (Rooms.quantity - func.coalesce(booked_rooms.c.rooms_booked, 0)).label("rooms_left"),
            )
            .join(booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True)
            .where(
                Rooms.hotel_id == hotel_id
            )
        )
        async with async_session_maker() as session:
            rooms = await session.execute(get_rooms)
        return rooms.mappings().all()
