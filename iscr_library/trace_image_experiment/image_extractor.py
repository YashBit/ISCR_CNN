import cv2
import numpy as np
from pdf2image import convert_from_path
import os

def convert_pdf_to_image(pdf_path, output_image_path):
    images = convert_from_path(pdf_path)
    if len(images) != 1:
        raise ValueError("PDF must contain exactly one page.")
    image_path = f"{output_image_path}_page.png"
    images[0].save(image_path, 'PNG')
    return image_path

def extract_image_with_padding(image_path, output_image_path, 
                               left_padding=10, right_padding=40, 
                               top_padding=10, bottom_padding=60):
    open_cv_image = cv2.imread(image_path)
    height, width, _ = open_cv_image.shape

    x_min = int(width * (left_padding / 100))
    x_max = int(width * (1 - (right_padding / 100)))
    y_min = int(height * (top_padding / 100))
    y_max = int(height * (1 - (bottom_padding / 100)))

    extracted_image = open_cv_image[y_min:y_max, x_min:x_max]
    output_file = f"{output_image_path}_extracted.png"
    cv2.imwrite(output_file, extracted_image)
    print(f"Saved extracted image to: {output_file}")

if __name__ == "__main__":
    pdf_path = "a_trace.pdf"  
    output_image_path = "extracted_image"  
    image_path = convert_pdf_to_image(pdf_path, output_image_path)
    extract_image_with_padding(image_path, output_image_path, 
                               left_padding=15, right_padding=40, 
                               top_padding=10, bottom_padding=60)
    os.remove(image_path)
