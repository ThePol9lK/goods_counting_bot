from pydantic import BaseModel


class User(BaseModel):
    name: str
    id_telegram: str
    admin: bool

