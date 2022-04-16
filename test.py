import streamlit as st
import cv2
import matplotlib.pyplot as plt
from PIL import Image

st.write(""" # Welcome to VASSAV Test App ! # """)

cv2_image = cv2.imread("C:/Users/harisathwik/Desktop/Apple.jpg")
cv2_convert = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:/Users/harisathwik/Desktop/Gray_Apple.jpg",cv2_convert)

with open("C:/Users/harisathwik/Desktop/Gray_Apple.jpg", "rb") as image:
    st.download_button(label="OUTPUT", data=image, file_name="output.png", mime="image/png")
    

    
