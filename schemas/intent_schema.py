from pydantic import BaseModel
from typing import List, Optional


class IntentSchema(BaseModel):
    app_type: str
    features: List[str]
    roles: List[str]
    monetization: Optional[List[str]] = []
    integrations: Optional[List[str]] = []