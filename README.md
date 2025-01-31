# Iris Recognition System

## Description
This project focuses on the precise identification of individuals using their irises. By leveraging the unique characteristics of the iris, we develop a biometric system capable of reliably and efficiently authenticating individuals. The project consists of two main phases: enrollment and recognition.

## Technologies Used

- **Programming Language**: Python
- **Python Libraries**:
  - **OpenCV**: For image processing and feature extraction.
  - **Pandas**: For data manipulation.
  - **NumPy**: For mathematical operations.
  - **Tkinter**: For developing the graphical interface.

## Features
- Iris image acquisition from the UPOL Iris Database
- Image pre-processing including grayscale conversion and histogram equalization
- Feature extraction using SIFT algorithm
- Correspondence module for comparing iris features using Euclidean distance
- Decision module for individual identification
- User-friendly graphical interface

## Project Structure
```
.
├── Data/
├── _pycache_/
├── database/
├── pictures_interface/
├── I1.png
├── I2.png
├── I3.png
├── correspondance.py
├── extraction.py
├── interface.py
├── requirements.txt
├── tempCodeRunnerFile.py
├── test_not_in_database.png
└── test_not_in_database2.png
```

## Installation
1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the main interface script:
```
python interface.py
```

## Modules
- `extraction.py`: Handles feature extraction using SIFT
- `correspondance.py`: Manages feature matching between iris images using Euclidean distance
- `interface.py`: Implements the graphical user interface

## Database
The project uses the UPOL Iris Database, which consists of 3 x 128 iris images (3 x 64 left and 3 x 64 right).

## Methods Used
- Feature Extraction: SIFT Detector and Descriptor (OpenCV)
- Correspondence: Euclidean Distance (OpenCV)

## Graphical Interface
The interface includes:
- A field to input the query image
- A display area for image processing steps and feature matching
- A field to display the acceptance or rejection decision

## Dependencies
See `requirements.txt` for a full list of dependencies. The main library used is OpenCV.

## Development
Development Language: Python


## Future Improvements
-Optimization of image processing algorithm parameters.
-Integration of machine learning techniques for more accurate identification.
-Extension of the system to support additional identification modalities.
