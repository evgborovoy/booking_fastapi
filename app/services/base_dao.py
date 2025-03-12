from sqlalchemy import select, insert, delete

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).filter_by(id=model_id))
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            result = await session.execute(select(cls.model).filter_by(**filter_by))
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            result = await session.execute(
                select(cls.model.__table__.columns)
            )
            return result.mappings().all()

    @classmethod
    async def create(cls, **data):
        async with async_session_maker() as session:
            await session.execute(insert(cls.model).values(**data))
            await session.commit()

    @classmethod
    async def delete(cls, **filter_by):
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
