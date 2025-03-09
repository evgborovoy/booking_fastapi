from app.services.base_dao import BaseDAO
from app.bookings.models import Bookings


class BookingDAO(BaseDAO):
    model = Bookings
