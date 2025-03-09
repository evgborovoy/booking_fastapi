from app.services.base_dao import BaseDAO
from app.users.models import Users


class UsersDao(BaseDAO):
    model = Users
