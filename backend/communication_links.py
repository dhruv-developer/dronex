from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get("/")
async def get_communication_links():
    df = pd.read_csv("app/data/indian_ocean_communication_links.csv")
    return df.to_dict(orient="records")
