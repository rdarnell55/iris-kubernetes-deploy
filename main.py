from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load the trained model
with open("iris_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/", response_class=HTMLResponse)
async def form_get(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/", response_class=HTMLResponse)
async def form_post(
    request: Request,
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    classes = ["Setosa", "Versicolor", "Virginica"]
    return templates.TemplateResponse("form.html", {
        "request": request,
        "result": f"Iris class: {classes[prediction]}"
    })

# For local testing
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)