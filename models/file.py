from pydantic import BaseModel

class File(BaseModel):
    id: int
    filename: str
    url: str
