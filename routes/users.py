from fastapi import APIRouter, HTTPException, status
from schemas.user import User

router = APIRouter(prefix="/users", tags=["Users"])

# In-memory user store (temporary, until DB is added)
users_db = []

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    # Check if email already exists
    for u in users_db:
        if u.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
    users_db.append(user)
    return {"message": "User created successfully", "user": user}
