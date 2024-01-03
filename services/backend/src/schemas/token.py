from typing import Optional
from pydantic import BaseModel

class TokenData(BaseModel):
    username: Optional[str] = None #vérifie que le token est de type string
    
class Status(BaseModel):
    message: str #envoie le message du status à l'utilisateur