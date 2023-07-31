import streamlit as st
from PIL import Image

# start the camera
camera_image = st.camera_input("Camera")

# create a pillow image instance
img = Image.open(camera_image)

# convert the pillow image to gray scale
gray_img = img.convert("L")

# Render the grayscale image image on the webpage
st.image(gray_img)

