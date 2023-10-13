from pydantic import BaseModel


class Product(BaseModel):
    name: str
    count: int
    description: str
    image: str
    id_category: int
