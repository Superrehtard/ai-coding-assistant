from pydantic import BaseModel
from typing import List


class ExplainRequest(BaseModel):
    code: str
    language: str | None = None


class ExplainResponse(BaseModel):
    explanation: str
    improvements: List[str]
    edge_cases: List[str]
