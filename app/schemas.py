from pydantic import BaseModel, EmailStr


class Registration(BaseModel):
    email: EmailStr


class Authorization(Registration):
    code: str


class CodeReturn(BaseModel):
    code: str


class ResultReturn(BaseModel):
    result: str
