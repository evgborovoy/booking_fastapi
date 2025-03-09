from pydantic import BaseModel, EmailStr, Field


class SUserAuth(BaseModel):
    email: EmailStr = Field(examples=["test@test.com"])
    password: str = Field(examples=["test"])
