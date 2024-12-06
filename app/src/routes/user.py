from fastapi import APIRouter
from app.src.crud.user import HelloWorld
router = APIRouter()

@router.get("/")
def read_root():
    return HelloWorld()