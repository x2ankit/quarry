from pydantic import BaseModel

class DocumentCreate(BaseModel):
    filename: str


class DocumentResponse(BaseModel):
    id: int
    filename: str

    model_config = {
        "from_attributes": True
    }