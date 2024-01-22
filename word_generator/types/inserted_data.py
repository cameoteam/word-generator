from pydantic import BaseModel
from typing import Literal


class InsertedData(BaseModel):
    key: str
    category: Literal[
        "image",
        "text",
    ]
    value: str
