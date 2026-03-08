from pydantic import BaseModel, ConfigDict
from typing import Optional

class ProfileSchema(BaseModel):
    id: str
    fullName: str
    email: str
    phone: str
    password: Optional[str] = None
    model_config = ConfigDict(extra='ignore')


class LoginSchema(BaseModel):
    email: str
    password: str
    model_config = ConfigDict(extra='ignore')
