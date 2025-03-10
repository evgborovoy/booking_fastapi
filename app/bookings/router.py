from fastapi import APIRouter, Depends

from app.bookings.schemas import SBookings
from app.bookings.service import BookingDAO
from app.users.dependecies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookings]:
    return await BookingDAO.find_all(user_id=user.id)
