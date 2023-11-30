from pydantic import BaseModel
from typing import Optional

class ApiResponseSchema(BaseModel):
    status: int
    message: str
    id_cia: Optional[str] = None
    timestamp: Optional[str] = None

    model_config = {
        "json_schema_extra": {
            "examples": [{
                    "status": "1",
                    "message": "Success",
            }]
        }
    }