from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np

app = FastAPI()
model = joblib.load("iris_model.pkl")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <body>
            <h2>Iris Prediction Form</h2>
            <form action="/predict/" method="post">
                <label>Sepal Length:</label><input type="text" name="sepal_length"><br>
                <label>Sepal Width:</label><input type="text" name="sepal_width"><br>
                <label>Petal Length:</label><input type="text" name="petal_length"><br>
                <label>Petal Width:</label><input type="text" name="petal_width"><br>
                <input type="submit" value="Predict">
            </form>
        </body>
    </html>
    """

@app.post("/predict/", response_class=HTMLResponse)
async def predict(
    sepal_length: float = Form(...),
    sepal_width: float = Form(...),
    petal_length: float = Form(...),
    petal_width: float = Form(...)
):
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(features)[0]
    return f"<h3>Predicted Class: {prediction}</h3>"