from fastapi import APIRouter

from app.bookings.schemas import SBookings
from app.bookings.service import BookingDAO

router = APIRouter(prefix="/bookings", tags=["Bookings"])

@router.get("")
async def get_bookings() -> list[SBookings]:
    return await BookingDAO.find_all()