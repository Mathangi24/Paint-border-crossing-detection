# Paint-border-crossing-detection

This Python script analyzes an image captured by a paint dispensing system to determine if the paint has crossed designated boundaries using the OpenCV library.
Requirements
Python 3.x
OpenCV

Installation
Install OpenCV:

pip install opencv-python

Place Your Image:
Place the image you want to analyze in the project directory.
Update the image_path variable in the script to the path of your image.
Usage

Edit the Script:
Open paint_boundary_analyzer.py.
Update the image_path variable with the path to your image file.
Adjust the boundary_top_left and boundary_bottom_right variables to set the coordinates of your boundary rectangle.

Run the Script:
python paint_boundary_analyzer.py
View the Results:

The script will print whether the paint has crossed the designated boundaries.
An image with the boundary rectangle will be displayed for visualization. Close the window to end the script.

Script Explanation
Load the Image: The script loads the image using cv2.imread.
Define the Boundaries: Specify the coordinates of the top-left and bottom-right corners of the boundary rectangle.
Draw the Boundary: The boundary is drawn on the image for visualization purposes.
Convert to Grayscale and Threshold: The image is converted to grayscale and then to a binary image using a threshold.
Find Contours: The contours of the paint area are found in the binary image.
Check Boundaries: The script checks if any point of the contours falls within the specified boundary.
Display Result: The result is printed, and the image with the boundary is displayed for verification.
Example
Image Path:
image_path = 'path_to_your_image.jpg'  # Replace with the path to your image
Boundary Coordinates:

boundary_top_left = (50, 50)
boundary_bottom_right = (200, 200)

Output:
Paint has crossed the designated boundaries.


Acknowledgments
This script uses the OpenCV library for image processing tasks.
