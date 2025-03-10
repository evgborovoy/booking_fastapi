from datetime import date

from fastapi import APIRouter

from app.rooms.schemas import SRoomInfo
from app.rooms.service import RoomDAO

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
        hotel_id: int, date_from: date, date_to: date) -> list[SRoomInfo]:
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms
