from pydantic import BaseModel


class Transaction(BaseModel):
    id_user: int
    id_product: int
    description: str
    count: int
