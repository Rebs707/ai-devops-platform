from fastapi import FastAPI

from app.api.devops import router as devops_router


app = FastAPI(
    title="AI DevOps Platform",
    version="1.0.0"
)


app.include_router(
    devops_router,
    prefix="/devops",
    tags=["DevOps"]
)


@app.get("/health")
def health():

    return {
        "status": "healthy",
        "platform": "AI DevOps Platform"
    }
