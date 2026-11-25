from fastapi import FastAPI

app = FastAPI(title="Labsphere")


@app.get("/")
def root():
    return{
        "project":"Labsphere",
        "message":"Hello Labsphere"
    }