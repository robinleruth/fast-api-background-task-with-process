from pydantic import BaseModel
from typing import List


class Trade(BaseModel):
    ticker: str
    price: float


class Client(BaseModel):
    name: str
    trades: List[Trade]


class Output(BaseModel):
    name: str
    number_of_trades: int
