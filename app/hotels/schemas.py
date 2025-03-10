from pydantic import BaseModel, Field


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list[str]
    room_quantity: int
    image_id: int


class SHotelInfo(SHotel):
    rooms_left: int

    class Config:
        from_attributes = True
