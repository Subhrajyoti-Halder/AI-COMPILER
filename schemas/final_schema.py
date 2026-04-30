from pydantic import BaseModel
from typing import List, Dict


class UIPageSchema(BaseModel):
    name: str
    components: List[str]


class APISchema(BaseModel):
    path: str
    method: str
    description: str


class DBTableSchema(BaseModel):
    name: str
    fields: List[str]


class FinalSchema(BaseModel):
    ui_pages: List[UIPageSchema]
    api_endpoints: List[APISchema]
    db_tables: List[DBTableSchema]
    auth_rules: Dict[str, List[str]]