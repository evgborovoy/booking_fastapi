from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.schemas import SHotelInfo
from app.hotels.service import HotelDAO

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("/{location}")
@cache(expire=10)
async def get_hotels_by_location(location: str, date_from: date, date_to: date) -> list[SHotelInfo]:
    hotels = await HotelDAO.find_all(location, date_from, date_to)
    return hotels
