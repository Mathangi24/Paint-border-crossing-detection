!pip install opencv-python
import cv2
import numpy as np
from google.colab.patches import cv2_imshow
# Load the image
image_path = '/content/paint.PNG'  # Replace with the path to your image
image = cv2.imread(image_path)
# Define the boundaries (example boundaries, you need to adjust based on your specific case)
boundary_top_left = (50, 50)
boundary_bottom_right = (200,200)
# Draw the boundary on the image (for visualization purposes)
boundary_color = (0, 255, 0)  # Green color in BGR
boundary_thickness = 2
cv2.rectangle(image, boundary_top_left, boundary_bottom_right, boundary_color, boundary_thickness)
# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to get a binary image
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
# Find contours in the binary image
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Check if any paint crosses the boundaries
paint_crossed_boundary = False
for contour in contours:
    for point in contour:
        x, y = point[0]
        if boundary_top_left[0] <= x <= boundary_bottom_right[0] and boundary_top_left[1] <= y <= boundary_bottom_right[1]:
            paint_crossed_boundary = True
            break
    if paint_crossed_boundary:
        break

  # Display the result
if paint_crossed_boundary:
    print("Paint has crossed the designated boundaries.")
else:
    print("Paint is within the designated boundaries.")

# Display the image with boundary for visualization
cv2_imshow(image)
cv2.waitKey(0)
cv2.destroyAllWindows()
