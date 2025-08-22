# wine-quality-pred

📊 Wine Quality Prediction App

This is a simple Flask web application that predicts wine quality using a pre-trained machine learning model. It provides a form for users to enter wine attributes and returns a predicted quality score.

🚀 Features

Built with Python, Flask, and Scikit-learn.
Dockerized for easy deployment.
Simple and interactive web UI.
Predicts red and white wine quality based on physicochemical inputs.

🐳 Run the App with Docker

1. Clone the repository

git clone https://github.com/RCC0149/wine-quality-pred.git
cd wine-quality-pred

2. Build the Docker image

docker build -t wine-quality-pred .

3. Run the container

docker run -p 5000:5000 wine-quality-pred

Then open your browser and go to: http://localhost:5000

📁 File Structure
.
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build instructions
├── scaler.pkl           # Scaler used in preprocessing
├── wine_model.pkl       # Trained ML model
├── templates/           # HTML templates
│   └── index.html

🧪 Model Inputs

The model expects the following inputs (typical wine characteristics):

Fixed acidity
Volatile acidity
Citric acid
Residual sugar
Chlorides
Free sulfur dioxide
Total sulfur dioxide
Density
pH
Sulphates
Alcohol

📷 Submission Instructions

Docker container successfully built (see screenshot)
This repository contains all required code and assets.

🧠 Note

Due to current compatibility issues with Heroku’s container registry, the app is not deployed there. This project is instead intended to run locally in Docker.
