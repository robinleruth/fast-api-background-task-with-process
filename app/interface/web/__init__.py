from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.config import app_config


api = FastAPI(title='API',
              description='',
              version='0.1')

from .controllers import some_controller
api.include_router(some_controller.router,
                   prefix='/api/v1/some_controller',
                   tags=['some_controller'])


api.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
