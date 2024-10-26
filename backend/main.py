from fastapi import FastAPI
import drones, mission_update, communication_links

app = FastAPI()

app.include_router(drones.router, prefix="/drones", tags=["Drones"])
app.include_router(mission_update.router, prefix="/mission_update", tags=["Mission Update"])
app.include_router(communication_links.router, prefix="/communication_links", tags=["Communication Links"])

@app.get("/")
async def root():
    return {"message": "Drone Swarm Coordination System API"}
