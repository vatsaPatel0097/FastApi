from fastapi import FastAPI

app = FastAPI()

@app.get('/Hello')
def Hello():
    return "Hello World"