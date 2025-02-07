import os 
import cv2
import numpy as np
def preprocess_xray(image_path, target_size=(224, 224)):
   #load the image
   image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
   # cv2.IMREAD_GRAYSCALE: Loads image in grayscale mode ( a flag used in OpenCV's cv2.imread() function to specify how the image should be loaded.)
   if image is None or image.size == 0:
            print(f"❌ Skipping corrupted image: {image_path}")
            return None
   #resize the image
   image_resized = cv2.resize(image, target_size)
   #normalize the image
   image_normalized = image_resized / 255.0
   return image_normalized
# Directory containing images
dataset_dir = "D:\Datasets\Fracture-multi-region-x-ray-data\Bone_Fracture_Binary_Classification\Bone_Fracture_Binary_Classification\Train"

# List to store processed images
processed_images = []
image_names = []  # Store filenames for display

# Process all images in the dataset
for subfolder in ["fractured", "not_fractured"]:
    subfolder_path = os.path.join(dataset_dir, subfolder)
    
    if not os.path.exists(subfolder_path):
        print(f"❌ Error: Subfolder '{subfolder}' not found in {dataset_dir}")
        continue

    for filename in os.listdir(subfolder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):  # Only process images
            image_path = os.path.join(subfolder_path, filename)
            processed_image = preprocess_xray(image_path)

            if processed_image is not None:
                processed_images.append(processed_image)
                image_names.append(filename)
                


# Display the first 3 processed images
for i in range(min(3, len(processed_images))):  
    cv2.imshow(f"Example {i+1}: {image_names[i]}", processed_images[i])
    cv2.waitKey(0)  
    cv2.destroyAllWindows()

# Check how many images were processed
print(f"\n✅ Total images processed: {len(processed_images)}") 


