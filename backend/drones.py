from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/")
async def get_drones():
    df = pd.read_csv("app/data/indian_navy_drone_specs.csv")
    return df.to_dict(orient="records")
