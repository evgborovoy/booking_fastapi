from datetime import date

from fastapi import APIRouter
from fastapi_cache.decorator import cache

from app.hotels.schemas import SHotelInfo
from app.hotels.service import HotelDAO

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
@cache(expire=30)
async def get_all_hotels():
    hotels = await HotelDAO.find_all()
    return hotels


@router.get("/{location}")
@cache(expire=10)
async def get_hotels_by_location(location: str, date_from: date, date_to: date) -> list[SHotelInfo]:
    hotels = await HotelDAO.find_all_by_location(location, date_from, date_to)
    return hotels
