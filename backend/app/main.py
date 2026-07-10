from fastapi import FastAPI

app = FastAPI(title="Vinted CRM")


@app.get("/")
def root():
    return {
        "message": "Vinted CRM API"
    }
