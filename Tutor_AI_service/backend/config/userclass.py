from pydantic import BaseModel


class UserClass(BaseModel):
    messages: str
