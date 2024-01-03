from typing import Optional
from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Notes

#Création de notes
NoteInSchema = pydantic_model_creator(
    Notes, name="NoteIn", exclude=["author_id"], exclude_readonly=True
)
#Récupération des notes
NoteOutSchema  = pydantic_model_creator(
    Notes, name="Note", exclude=["modified_at", "author.password", "author.created_at", "author.modified_at"]
)

#Mise à jour des notes
class UpdateNote(BaseModel):
    title: Optional[str]
    content: Optional[str]