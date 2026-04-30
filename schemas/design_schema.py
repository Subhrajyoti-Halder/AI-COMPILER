from pydantic import BaseModel
from typing import List


class FlowSchema(BaseModel):
    name: str
    steps: List[str]


class ModuleSchema(BaseModel):
    name: str
    description: str


class PermissionSchema(BaseModel):
    role: str
    permissions: List[str]


class DesignSchema(BaseModel):
    entities: List[str]
    flows: List[FlowSchema]
    modules: List[ModuleSchema]
    permissions: List[PermissionSchema]