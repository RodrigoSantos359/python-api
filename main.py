from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/process")
def process(data: dict):
    df = pd.DataFrame(data["items"])
    df["sum"] = df.select_dtypes("number").sum(axis=1)

    return {
        "result": df.to_dict(orient="records")
    }