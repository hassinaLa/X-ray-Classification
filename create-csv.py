import os
import csv

# Define dataset paths
dataset_path = dataset_path = dataset_path = "D:/Datasets/fracture-multi-region-x-ray-data/Bone_Fracture_Binary_Classification/Bone_Fracture_Binary_Classification"


splits = ["train", "val", "test"]

# Labels mapping
label_mapping = {"fractured": 1, "not_fractured": 0}

# Function to create CSV
def create_csv(split):
    csv_file = os.path.join(dataset_path, f"{split}_labels.csv")
    split_path = os.path.join(dataset_path, split)
    
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["image_path", "label"])
        
        for label_name, label_value in label_mapping.items():
            folder_path = os.path.join(split_path, label_name)
            for image_name in os.listdir(folder_path):
                image_path = os.path.join(split, label_name, image_name)
                writer.writerow([image_path, label_value])

# Generate CSVs for all splits
for split in splits:
    create_csv(split)

print("CSV files created!")

