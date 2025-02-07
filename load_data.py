import pandas as pd
import os
import cv2

def load_csv(file_path):
    """
    Load the CSV file and print the first few rows.
    """
    data = pd.read_csv(file_path)
    print(data.head())  # Display the first few rows for verification
    return data

if __name__ == "__main__":
    # Define paths
    csv_file = "D:/Datasets/fracture-multi-region-x-ray-data/Bone_Fracture_Binary_Classification/Bone_Fracture_Binary_Classification/train_labels.csv"
    root_dir = "D:/Datasets/fracture-multi-region-x-ray-data/Bone_Fracture_Binary_Classification/Bone_Fracture_Binary_Classification"
    
    # Load the CSV
    train_data = load_csv(csv_file)
    
    # Display a few images with their labels
    for i in range(5):  # Display 5 examples
        image_path = os.path.join(root_dir, train_data.iloc[i]['image_path'])
        label = train_data.iloc[i]['label']
        
        # Load and display the image
        image = cv2.imread(image_path)
        label_text = "Fractured" if label == 1 else "Not Fractured"
        
        # Display the image with a title
        cv2.imshow(f"Label: {label_text}", image)
        
        # Wait for a key press and close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
