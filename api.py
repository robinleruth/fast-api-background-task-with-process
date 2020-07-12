import uvicorn

from app.interface.web import api

api = api

if __name__ == '__main__':
    uvicorn.run(api)
