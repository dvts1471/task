from typing import Literal

from core.api.api_base_model import ApiBaseModel


class PlaceBetDto200(ApiBaseModel):
    message: str
    matchId: str
    selection: str
    stake: float
    odds: float
    payout: float
    balance: float
    currency: str


class PlaceBetDto405(ApiBaseModel):
    error: Literal["insufficient_balance"]
    message: str
