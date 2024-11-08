

import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set up pytesseract path (Adjust this path to where Tesseract is installed on your machine)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Super\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Load the image from the path
    img = cv2.imread(image_path)

    # Convert to grayscale for better OCR results
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to get a clear text
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Optional: Resize image if text is small
    scale_percent = 150  # percent of original size
    width = int(thresh.shape[1] * scale_percent / 100)
    height = int(thresh.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(thresh, dim, interpolation=cv2.INTER_LINEAR)

    return resized

def extract_text_from_image(image_path):
    # Preprocess the image
    processed_image = preprocess_image(image_path)

    # Convert processed image to PIL format (required by pytesseract)
    pil_img = Image.fromarray(processed_image)

    # Perform OCR on the processed image
    extracted_text = pytesseract.image_to_string(pil_img, lang='eng')

    return extracted_text

# Example usage
image_path = 'card.jpg'  # Replace with your image path
text = extract_text_from_image(image_path)

# Print extracted text to console
print("Extracted Text:", text)

# Save extracted text to a file
output_file = 'extracted_text.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Text has been saved to {output_file}")
