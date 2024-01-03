from tortoise.contrib.pydantic import pydantic_model_creator
from src.database.models import Users

#Nouveaux users
UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)
#Retour aux users finaux
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
#validation des Users
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)