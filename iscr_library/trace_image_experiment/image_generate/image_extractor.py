import cv2
import numpy as np
from pdf2image import convert_from_path
import os
import re

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
    output_file = f"{output_image_path}.png"
    cv2.imwrite(output_file, extracted_image)
    print(f"Saved extracted image to: {output_file}")

def process_pdfs(directory):
    normal_counter = 1
    trace_counter = 1
    normal_folder = os.path.join(directory, "normal_letters_images")
    trace_folder = os.path.join(directory, "trace_letters_images")
    
    if not os.path.exists(normal_folder):
        os.makedirs(normal_folder)
    if not os.path.exists(trace_folder):
        os.makedirs(trace_folder)
    
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            normal_match = re.match(r"([a-z])_([a-z]+)_([a-z]+)_([0-9.]+)\.pdf", filename)
            trace_match = re.match(r"([a-z])_trace_([a-z]+)_([0-9.]+)_([a-z]+)\.pdf", filename)
            
            if normal_match:
                letter, font_name, typeface, size = normal_match.groups()
                output_image_path = os.path.join(normal_folder, f"{letter}_{normal_counter}")
                normal_counter += 1
            elif trace_match:
                letter, font_name, size, typeface = trace_match.groups()
                output_image_path = os.path.join(trace_folder, f"{letter}_{trace_counter}")
                trace_counter += 1
            else:
                continue  # Skip files that don't match the expected formats

            image_path = convert_pdf_to_image(pdf_path, output_image_path)
            extract_image_with_padding(image_path, output_image_path, 
                                       left_padding=15, right_padding=40, 
                                       top_padding=10, bottom_padding=60)
            os.remove(image_path)

if __name__ == "__main__":
    process_pdfs("/path/to/your/pdf/folder")
