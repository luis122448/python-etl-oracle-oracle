from pydantic import BaseModel
from typing import Optional

class EtlBasic(BaseModel):
    id_cia: str
    
    model_config = {
        "json_schema_extra": {
            "examples": [{
                    "id_cia": "66"
                }]
        }
    }