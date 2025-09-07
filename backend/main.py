from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings

# Instantiate FastAPI instance
app = FastAPI(
    title="SalaryBoy API",
    description="API to fetch salary records and stats",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Allows API to be used from a different origin
# allows frontend and backend to communicate
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"], # POST, GET, PUT, DELETE
    allow_headers=["*"],
)
 

if __name__ == "__main__":
    import uvicorn # uvicorn is the webserver, runs the FastAPI API
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)