import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException

from src.endpoints.users.router import router as users_router
from src.endpoints.tasks.router import router as tasks_router

app = FastAPI(
    title="TP2024",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)


@app.get("/ping")
async def pong():
    return {"ping": "pong"}


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


if __name__=="__main__":
    uvicorn.run("main:app", host='localhost', port=8000, reload=True)


app.include_router(users_router, tags=["Users"], prefix="/api/users")
app.include_router(tasks_router, tags=["Tasks"], prefix="/api/tasks")
