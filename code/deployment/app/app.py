import streamlit as st
import requests
from PIL import Image
import io

st.title("Image Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button("Predict"):
        image_bytes = io.BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes = image_bytes.getvalue()

        files = {"file": ("image.png", image_bytes, "image/png")}
        response = requests.post("http://api:8000/predict", files=files)
        
        if response.status_code == 200:
            result = response.json()
            predicted_jellyfish = result.get('predicted_jellyfish')
            confidence = result.get('confidence')

            st.write(f"Predicted Jellyfish: {predicted_jellyfish}")
            st.write(f"Confidence: {confidence:.2f}")
        else:
            st.write("Error: Unable to get prediction.")
