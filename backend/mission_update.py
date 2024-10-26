from fastapi import APIRouter, Request
import aco_model, pso_model

router = APIRouter()

@router.post("/")
async def mission_update(request: Request):
    data = await request.json()
    aco_result = aco_model.optimize(data)
    pso_result = pso_model.optimize(data)
    return {"ACO": aco_result, "PSO": pso_result}
