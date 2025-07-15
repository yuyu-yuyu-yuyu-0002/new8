from pydantic import BaseModel

class Storage(BaseModel):
    id: int
    type: str
    capacity: int
