from pydantic import BaseModel
from typing import Optional

class AnalyzeRequest(BaseModel):
    text: str
    url: Optional[str] = None
    