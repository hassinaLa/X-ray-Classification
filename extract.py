import cv2
import numpy as np
import os

def extract_edges(image_path, target_size=(224, 224)):
    """
    Loads an X-ray image, converts it to grayscale, resizes, normalizes, and applies Canny edge detection.
    Returns the edge-detected image.
    """
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print(f"❌ Error: Unable to load image at {image_path}")
        return None

    # Resize the image
    image_resized = cv2.resize(image, target_size)

    # Apply Canny Edge Detection
    edges = cv2.Canny(image_resized, threshold1=50, threshold2=150)

    return edges

# ✅ Test with some images
dataset_dir = "D:\Datasets\Fracture-multi-region-x-ray-data\Bone_Fracture_Binary_Classification\Bone_Fracture_Binary_Classification\Train"

# Process a few images
for subfolder in ["fractured", "not_fractured"]:
    subfolder_path = os.path.join(dataset_dir, subfolder)

    for filename in os.listdir(subfolder_path)[:3]:  # Process only 3 images per category
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(subfolder_path, filename)
            edges = extract_edges(image_path)

            if edges is not None:
                cv2.imshow(f"Edges - {filename}", edges)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
