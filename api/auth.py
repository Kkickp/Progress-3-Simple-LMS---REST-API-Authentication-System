from ninja import Router
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from courses.models import User
from .schemas import UserRegisterSchema, LoginSchema
from .utils import create_access_token

router = Router()


@router.post("/register")
def register(request, payload: UserRegisterSchema):

    user = User.objects.create(
        username=payload.username,
        password=make_password(payload.password),
        role=payload.role
    )

    return {"message": "User created", "id": user.id}


@router.post("/login")
def login(request, payload: LoginSchema):

    user = authenticate(
        username=payload.username,
        password=payload.password
    )

    if not user:
        return {"error": "Invalid credentials"}

    token = create_access_token({"user_id": user.id})

    return {"access_token": token}