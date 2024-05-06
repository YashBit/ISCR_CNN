from ultralytics import YOLO
import cv2 

model = YOLO('yolov8n.pt')
results = model("/Users/yashbharti/Desktop/ISCR_CNN/data/images/image_dataset_1/Traffic-3IH35.jpeg", show = True)
cv2.waitKey(0)


