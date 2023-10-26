import streamlit as st
from PIL import Image
import pytesseract
import re

# Define a function to extract and sum numbers from text
def extract_and_sum_numbers(text):
    numbers = re.findall(r'\d{1,3}(?:,\d{3})*(?:\.\d+)?', text)
    numbers = [int(num.replace(',', '')) for num in numbers]
    return sum(numbers)

def main():
    st.title("OCR Number Sum App")

    # Upload image
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform OCR
        text = pytesseract.image_to_string(image, lang='eng')

        st.write("Extracted Text:")
        st.write(text)

        # Extract and sum numbers
        total_sum = extract_and_sum_numbers(text)

        st.write("Sum of Numbers:", total_sum)

if __name__ == "__main__":
    main()
