from core.api.api_base_model import ApiBaseModel


class ResetBalanceDto200(ApiBaseModel):
    message: str
    balance: float
    currency: str
