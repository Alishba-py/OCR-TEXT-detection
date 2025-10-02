# OCR-TEXT-detection

## Project Overview
This project demonstrates **text extraction from images using Python and Tesseract OCR**. It takes an input image, preprocesses it for better OCR results, and extracts the text into a structured text file. This workflow can be extended for scanned documents, PDFs, or other image-based data sources.

## Folder Structure
OCR-TEXT-detection/
│
├── app.py # Main Python script for OCR extraction
├── card.jpg # Sample image for OCR
├── extracted_text.txt # Output text file after OCR
└── README.md # Project documentation


## Features
- Image preprocessing: grayscale, thresholding, resizing  
- OCR text extraction with Tesseract  
- Saves output to `extracted_text.txt`  
- Can be adapted for multiple images or PDFs  

## Requirements
- Python 3.x  
- OpenCV (`cv2`), Pillow (`PIL`), pytesseract, numpy  
- Tesseract OCR installed on your machine  

## Usage
1. Install dependencies:
```bash
pip install opencv-python pillow pytesseract numpy

## Set Tesseract path in app.py if needed
- pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Super\Tesseract-OCR\tesseract.exe'

Run the script:
python app.py

Extracted text will be printed and saved in extracted_text.txt.

Demo

Sample image (card.jpg) is included.

Output file extracted_text.txt shows extracted text.
