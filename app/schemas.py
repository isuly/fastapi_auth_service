from pydantic import BaseModel, EmailStr


class Registration(BaseModel):
    email: EmailStr


class Authorization(Registration):
    code: str
