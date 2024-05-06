"""

Rotation Script for 18 Variations for every single image


"""

from PIL import Image
import os 

source_folder = "/Users/yashbharti/Desktop/ISCR_CNN/data/images/image_dataset_1/different_shapes"

image_files = [f for f in os.listdir(source_folder) if f.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]

for image_file in image_files:
    image_path = os.path.join(source_folder, image_file)
    img = Image.open(image_path)

    for i in range(18):
        rotated_img = img.rotate(20 * (i + 1), expand = True)
        out_file = f"{os.path.splitext(image_file)[0]}_{20 * (i + 1)}{os.path.splitext(image_file)[1]}"
        rotated_img.save(os.path.join(source_folder, out_file))

        # Close the rotated image to free up resources
        rotated_img.close()

    # Close the original image
    img.close()

print("Rotation and saving complete.")