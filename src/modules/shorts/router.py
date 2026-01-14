from fastapi import APIRouter

router = APIRouter(prefix="/shorts", tags=["shorts"])

@router.get("/")
def get_shorts():
    return {"message": "List of shorts"}