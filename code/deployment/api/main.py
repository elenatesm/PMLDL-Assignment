from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
import numpy as np
import keras
import logging
import io

app = FastAPI()

model = keras.models.load_model("./api/models/model.keras")

jellyfish_names = ["Barrel Jellyfish", "Blue Jellyfish", "Compass Jellyfish", "Lions Mane Jellyfish", "Mauve Stringer Jellyfish", "Moon Jellyfish"]

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image = Image.open(io.BytesIO(await file.read()))
    
        image = image.resize((224, 224)) 
        image_array = np.array(image) / 255.0 
        image_array = np.expand_dims(image_array, axis=0)

        expected_input_shape = model.input_shape[1:]
        if image_array.shape[1:] != expected_input_shape:
            raise HTTPException(status_code=400, detail=f"Expected input shape {expected_input_shape}, got {image_array.shape[1:]}")

        prediction = model.predict(image_array)
        prediction = prediction[0]
        
        max_index = np.argmax(prediction)
        predicted_jellyfish = jellyfish_names[max_index]

        return {"predicted_jellyfish": predicted_jellyfish, "confidence": float(prediction[max_index])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
