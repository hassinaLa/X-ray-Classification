AI project:
1/ Defining the Scope of the Project:
-Objective: The goal is to classify X-ray images into two categories: broken or not broken.
-Output: A binary classification (fractured or not fractured).
-Considerations: if it goes well I'll consider localizing the fracture (i.e., pinpoint the location of the break)
AI-project/
├── create_csv.py       # Script for generating CSV files
├── load_data.py        # Script for loading and preparing data
├──  
2/ Data Collection:
-Dataset:
1. Bone Fracture Multi-Region X-ray Dataset:This dataset comprises both fractured and non-fractured X-ray images covering various anatomical regions, including the lower limb, upper limb, lumbar region, hips, and knees. It's organized into training, validation, and test sets, each containing both fractured and non-fractured images.
-Dataset Contents:
Training Data Number of Images: 9246
Validation Data Number of Images: 828
Test Data Number of Images: 506
3. Generate CSV Files 
The dataset is structured as:
dataset/
├── train/
│   ├── fractured/
│   │   ├── image1.png
│   │   ├── image2.png
│   └── not_fractured/
│       ├── image3.png
│       ├── image4.png
├── val/
│   ├── fractured/
│   └── not_fractured/
└── test/
    ├── fractured/
    └── not_fractured/
Each row looks like this:
image_path,label
train/fractured/image1.png,1
train/not_fractured/image2.png,0
4. Loading and preparing data


