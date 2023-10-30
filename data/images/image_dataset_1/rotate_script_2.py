from PIL import Image
import os

source_folder = "/Users/yashbharti/Desktop/ISCR_CNN/data/images/small_q_p_images"  # Adjust this path based on your dataset location in Google Drive

image_files = [f for f in os.listdir(source_folder) if f.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif"))]

for image_file in image_files:
    image_path = os.path.join(source_folder, image_file)
    img = Image.open(image_path)

    # List of angles for rotation
    angles = [45, 90, 180]

    # Rotate by the specified angles and save
    for angle in angles:
        rotated_img = img.rotate(angle, expand=True)
        out_file = f"{os.path.splitext(image_file)[0]}_{angle}{os.path.splitext(image_file)[1]}"
        rotated_img.save(os.path.join(source_folder, out_file))
        rotated_img.close()

    # Flip the image horizontally
    flipped_img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

    # Rotate the flipped image by the specified angles and save
    for angle in angles:
        rotated_flipped_img = flipped_img.rotate(angle, expand=True)
        out_file = f"{os.path.splitext(image_file)[0]}_flipped_{angle}{os.path.splitext(image_file)[1]}"
        rotated_flipped_img.save(os.path.join(source_folder, out_file))
        rotated_flipped_img.close()

    # Close the original and flipped images
    img.close()
    flipped_img.close()

print("Rotation, flipping, and saving complete.")
