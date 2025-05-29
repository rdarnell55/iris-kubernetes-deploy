# Iris Kubernetes Deployment

This project demonstrates the end-to-end deployment of a machine learning model (SVM classifier trained on the Iris dataset) using **FastAPI**, **Docker**, and **Kubernetes (via Minikube)**.

Yes, it's a flower classifier. But it's deployed like it’s a billion-dollar fintech API. ;)

---

## Project Overview

* Trained a **Support Vector Machine** (SVM) classifier on the classic Iris dataset
* Exposed a prediction API via a **FastAPI** app
* Created a basic **HTML UI** for user input
* Containerized the application with **Docker**
* Deployed the container using **Kubernetes**
* Validated deployment on **Minikube**
* Provided `.yaml` configuration files for reproducible deployment

---

## Files and Structure

```
.
├── app.py                    # FastAPI app logic
├── main.py                   # Entry point for FastAPI
├── iris_model.pkl            # Trained SVM model
├── iris_model_training.ipynb # Notebook to train/export the model
├── Dockerfile                # Docker container spec
├── requirements.txt          # Dependencies
├── templates/
│   └── index.html            # Simple UI form
├── k8s/
│   ├── deployment.yaml       # Kubernetes Deployment
│   └── service.yaml          # Kubernetes Service
└── README.md                 # This file
```

---

## How to Verify (Instructions for Instructor)

> Here’s everything you need to run and verify my work.

### Prerequisites

* Docker installed
* Minikube installed and running (`minikube start`)
* Kubernetes CLI (`kubectl`)
* Python 3.11+
* Git

### Clone the Repo

```bash
git clone https://github.com/rdarnell55/iris-kubernetes-deploy.git
cd iris-kubernetes-deploy
```

### Build Docker Image

```bash
docker build -t iris-api .
```

### (Optional) Re-train the model

If you're suspicious of `.pkl` files:

```bash
jupyter notebook iris_model_training.ipynb
# Run all cells to retrain and save iris_model.pkl
```

### Kubernetes Deployment

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check deployment:

```bash
kubectl get pods
kubectl get service
```

### Access the Web UI

```bash
minikube service iris-api-service
```

It will output a URL like:

```
http://127.0.0.1:PORT
```

Copy and paste into browser. You’ll see a form where you can test predictions.

### Here Are Some Sample Test Cases

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}  → Prediction: setosa

{
  "sepal_length": 6.7,
  "sepal_width": 3.1,
  "petal_length": 4.7,
  "petal_width": 1.5
}  → Prediction: versicolor

{
  "sepal_length": 7.2,
  "sepal_width": 3.6,
  "petal_length": 6.1,
  "petal_width": 2.5
}  → Prediction: virginica

---

## What I Learned

* Packaging ML models for real-world deployment
* Building REST APIs with FastAPI
* Containerizing with Docker
* Deploying services using Kubernetes and Minikube

---

## Notes

* The model was trained using scikit-learn 1.6.1; if loading fails, match that version
* ngrok was used during development to expose ports temporarily
* All secrets and sensitive data have been excluded (because there are none)

---

## Assignment Context

This project was developed for **ANA680 Module 4** at **National University**. The goal was to demonstrate the ability to serve and deploy a trained ML model using a containerized Kubernetes setup.

---

### Thanks for grading this. Seriously. You earned that coffee. :)
