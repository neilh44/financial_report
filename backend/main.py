from fastapi import FastAPI
from app.controllers.extraction_controller import router as extraction_router
from app.controllers.translation_controller import router as translation_router

app = FastAPI()

# Register routers
app.include_router(extraction_router, prefix="/api/extract", tags=["Extraction"])
app.include_router(translation_router, prefix="/api/translate", tags=["Translation"])

@app.get("/")
def read_root():
    return {"message": "Financial Report Analysis API is running"}
