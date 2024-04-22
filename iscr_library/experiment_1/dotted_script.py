import cv2
import numpy as np

image = cv2.imread('/Users/yashbharti/Desktop/Engineering/ISCR_CNN/iscr_library/experiment_1/b.png')
dot_size = 5
gap_size = 10

print("Process Started")
dot_size = 2

# Create a dot pattern with small round dots
dot_pattern = np.zeros((dot_size, dot_size), dtype=np.uint8)
cv2.circle(dot_pattern, (dot_size // 2, dot_size // 2), dot_size // 2, (255), -1)

# Resize the dot pattern to match the size of the input image
rows, cols, _ = image.shape
dot_pattern = cv2.resize(dot_pattern, (cols, rows), interpolation=cv2.INTER_NEAREST)

# Convert dot pattern to 3 channels to match the image
dot_pattern = cv2.merge([dot_pattern, dot_pattern, dot_pattern])

# Apply the dot pattern to the input image
dotted_image = cv2.bitwise_and(image, dot_pattern)

# Save the dotted image
cv2.imwrite('dotted_image.jpg', dotted_image)
print("Success")

