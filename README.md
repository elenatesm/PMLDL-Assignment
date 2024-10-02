# PMLDL-Assignment
PMLDL Assignment 1

This project is an image classifier that identifies different species of jellyfish using a ml model. The project is built using Keras for the model, FastAPI for serving the model as an API, and Streamlit for the user interface.

## Project Overview
The goal of this project is to classify jellyfish species based on image inputs. It uses a deep learning model trained on jellyfish images. The model is deployed through a REST API, and an easy-to-use frontend allows users to upload images and see predictions.

## Features
Model: A deep learning model trained using Keras.

API: A FastAPI backend for making predictions.

UI: A Streamlit interface for uploading images and visualizing predictions.

Dockerized: The project is containerized using Docker for easy deployment.

## Installation:
### Clone the Repository
```
git clone https://github.com/elenatesm/PMLDL-Assignment.git
cd PMLDL-Assignment
```

### Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # для Linux/Mac
.\venv\Scripts\activate  # для Windows
```

### Install the dependencies:
```
pip install -r requirements.txt
```

## Run the Project Locally

### 1. Start the API:
```
cd code/deployment/api
uvicorn api:app --reload
```

### 2. Run the Streamlit App:
In another terminal window, run:
```
cd code/deployment/app
streamlit run app.py
```

## Using Docker
Alternatively, you can run the project with Docker.

### Build the Docker image:
```
docker-compose build
```

### Run the Docker containers:
```
docker-compose up
```

## Usage
Open the Streamlit interface in your browser (http://localhost:5001).

Upload a jellyfish image.

Click on the "Predict" button.

The model will return the predicted jellyfish species with the corresponding confidence score.
