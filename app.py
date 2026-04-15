import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Set title
st.title("Kidney Stone Detection App")
st.write("Upload an X-ray or ultrasound image to check for Kidney Stone.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_container_width=True)

    # Preprocess the image
    img = img.resize((150, 150))  # use the same size as your model input
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Make prediction
    prediction = model.predict(img_array)

    # Show result
    class_label = "Stone" if prediction[0][0] >= 0.5 else "Normal"
    confidence = prediction[0][0] if class_label == "Stone" else 1 - prediction[0][0]

    st.write(f"### Prediction: *{class_label}*")
    st.write(f"Confidence: *{confidence:.2%}*")