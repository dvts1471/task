from dataclasses import dataclass
from typing import Type, Optional

from core.api.api_base_model import ApiBaseModel


@dataclass
class ApiExpectedResponse:
    status_code: int
    model: Optional[Type[ApiBaseModel]] = None
