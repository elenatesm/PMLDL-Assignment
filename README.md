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

## Run the Project Locally

To run app from the main directory of the project:

### Run the Docker containers:
```
cd code/deployment
docker-compose up --build
```

## Usage
Open the Streamlit interface in your browser (http://localhost:5001).

Upload a jellyfish image.

Click on the "Predict" button.

The model will return the predicted jellyfish species with the corresponding confidence score.
