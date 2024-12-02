from fastapi import APIRouter, Query
from ..controllers.add_cont import add_numbers

router = APIRouter(
    prefix='/maths',
    tags=['maths']
)

@router.post("/add", tags=['addition'])
def add_numbers_endpoint(num1: float = Query(...), num2: float = Query(...)):
    return add_numbers(num1, num2)