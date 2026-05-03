from pydantic import BaseModel
from requests import Response

class ApiBaseModel(BaseModel):
    class Config:
        case_sensitive= True
        extra = 'forbid'

    @classmethod
    def parse_response(cls, response: Response) -> 'ApiBaseModel':
        return cls.model_validate(response.json())

    def appears_in(self, model: BaseModel) -> bool:
        self_params_dict = self.model_dump()
        model_params_dict = model.model_dump()

        for k, v in self_params_dict.items():
            if not model_params_dict.get(k, None):
                return False
        return True