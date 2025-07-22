from pydantic import BaseModel, EmailStr, Field
from typing import Annotated, Optional

class User(BaseModel):
    name: Annotated[str, Field(..., description="Full name of the user", min_length=1)]
    email: Annotated[EmailStr, Field(..., description="Email address of the user")]
    password: Annotated[str, Field(..., description="Password", min_length=6)]
    phone: Annotated[Optional[str], Field(None, description="Optional phone number")]
