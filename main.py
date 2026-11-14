from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/about")
def about():
    return{"Developer": "Springbean", "Project": "Civic Report"}

@app.get("/category")
def category():
    return ["pothole", "illegal_dumping", "broken_streetlight", "flooding", "other"]