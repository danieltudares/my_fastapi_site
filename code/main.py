import fastapi
import uvicorn
from uvicorn.main import main

app = fastapi.FastAPI()


@app.get('/')
def index():
    return("Hello world")


if __name__ == '__main__':
    uvicorn.run(app)
