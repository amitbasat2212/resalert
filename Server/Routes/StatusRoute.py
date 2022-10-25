from fastapi import APIRouter

from Routes import ErrorHandling


router = APIRouter()

router = APIRouter(
    prefix="/pokemons",
    tags=["pokemons"]
)
