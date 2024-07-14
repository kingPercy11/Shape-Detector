# Shape Detector

This project is a simple shape detection system using OpenCV in Python. It processes images to detect various geometric shapes such as triangles, rectangles, squares, circles, and polygons with different numbers of sides.

## Features
- Detects and identifies shapes in an image.
- Supports detection of triangles, squares, rectangles, pentagons, hexagons, heptagons, octagons, nonagons, decagons, and circles.
- Draws contours around detected shapes and labels them.

## Prerequisites
- Python 3.x
- OpenCV
- numpy

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/shapedetector.git
    cd shapedetector
    ```

2. Install the required packages:
    ```bash
    pip install opencv-python numpy
    ```

## Usage
1. Place the image you want to process in the project directory.
2. Run the script:
    ```bash
    python shapedetector.py
    ```

3. Enter the path to the input image when prompted.

The script will process the image, detect shapes, and display the result with detected shapes labeled.

## Code Explanation
- **`cv2.findContours`**: Finds contours in the image to detect the boundaries of shapes.
- **`cv2.approxPolyDP`**: Approximates the contour to a simpler shape with fewer vertices.
- **`cv2.boundingRect`**: Calculates the bounding rectangle of a contour to determine the aspect ratio for distinguishing between squares and rectangles.
- **`cv2.contourArea`** and **`cv2.arcLength`**: Used to calculate the area and perimeter of the contour to identify circles based on circularity.
- **`cv2.drawContours`**: Draws contours on the image to mark the detected shapes.
- **`cv2.putText`**: Labels the detected shapes on the image.

## Example
```bash
Enter the path of the input image: path/to/your/image.jpg
