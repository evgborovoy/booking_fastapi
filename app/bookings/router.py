from datetime import date

from fastapi import APIRouter, Depends, status

from app.bookings.schemas import SBookings
from app.bookings.service import BookingDAO
from app.exceptions import RoomCannotBeBooked
from app.users.dependecies import get_current_user
from app.users.models import Users

from fastapi_cache.decorator import cache

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
@cache(expire=10)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def create_booking(room_id: int, date_from: date, date_to: date, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.create(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked


@router.delete("/{booking_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    await BookingDAO.delete(id=booking_id, user_id=user.id)