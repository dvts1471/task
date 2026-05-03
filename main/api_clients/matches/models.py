from pydantic import RootModel

from core.api.api_base_model import ApiBaseModel
from datetime import date

class Odds(ApiBaseModel):
    home: float
    draw: float
    away: float

class Match(ApiBaseModel):
    id: str
    competition: str
    kickoffDate: date
    homeTeam: str
    awayTeam: str
    odds: Odds

class GetAllMatchesDto200(RootModel[list[Match]]):
    ...
