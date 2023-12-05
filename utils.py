"""
Title: Util.py
Description: Utility functions

"""

import cv2
import os
import numpy as np

colors = {
    "blue": (),
    "red": (),
    "green": ()
}

# Plot keypoints with original image and keypoints
def plot_keypoints(image, keypoints, color=(0, 0, 255)):
    """ Plot keypoints on image """

    image_height, image_width, _ = image.shape
    # Loop over each keypoint
    for keypoint in keypoints:
        x = int(keypoint[0] * image_width)
        y = int(keypoint[1] * image_height)

        if len(keypoint) > 2:
            v = keypoint[2]

        # Plot the keypoints
        cv2.circle(image, (x, y), 5, color, -1)

    return image

# Plot keypoints according to image and label file
def plot_keypoints_file(image_path, label_path):
    # Load the image
    image = cv2.imread(image_path)
   
    # Read the labels from the label file
    with open(label_path, 'r') as file:
        labels = file.readlines()

    # Extract the keypoints from the label file 
    keypoints = []
    for label in labels:
        # Parse the label
        label_parts = label.split(' ')
        image_class = label_parts[0]
        bbox = [float(coord) for coord in label_parts[1:5]]
        keypoints = [float(coord) for coord in label_parts[5:-1]]

        # Make keypoints into tuples
        keypoints = [(keypoints[i], keypoints[i+1], keypoints[i+2]) for i in range(0, len(keypoints), 3)]

        # Draw the keypoints on the image
        plot_keypoints(image, keypoints)

    # Return Keypoint
    return image, keypoints

# Plot lines between keypoints 
def plot_lines(image, keypoints, grid):
    """ Plot lines between keypoints """
    # Define pairs of keypoints
    if grid == "tennis":
        pairs = [(0, 4), (4, 6), (6, 1), (0, 2), (4, 8), (8, 10), (10, 5), (6, 9), (9, 11), (11, 7), (1, 3), (8, 12), (12, 9), (10, 13), (13, 11), (2, 5), (5, 7), (7, 3), (12, 13)]
    elif grid == "basketball":
        pairs = [(0, 1), (1, 13), (13, 14), (14, 3), (3, 2), (2, 7), (7, 6), (6, 5), (5, 4), (4, 0), (5, 8), (6, 9), (8, 9)]
    

    image_height, image_width, _ = image.shape

    # Loop over each pair
    for i, j in pairs:
        # Draw line between keypoints[i] and keypoints[j]
        # if either of the keypoints is not visible, do not draw the line
        if keypoints[i][2] == 0 or keypoints[j][2] == 0:
            continue

        # Un-normalize the keypoints
        x1 = int(keypoints[i][0] * image_width)
        y1 = int(keypoints[i][1] * image_height)
        x2 = int(keypoints[j][0] * image_width)
        y2 = int(keypoints[j][1] * image_height)

        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return image

# KPS Refine

# Homography
def homography():
    """ Peform Homography on image to enhance keypoint location """

def flatten_perspective(image, keypoints):
    # Get four corners of the keypoints, 0, 

    # Define source points
    src_pts = np.float32(keypoints)

    # Define destination points
    dst_pts = np.float32([[0, 0], [image.shape[1] - 1, 0], [image.shape[1] - 1, image.shape[0] - 1], [0, image.shape[0] - 1]])
    print(dst_pts)
    
    # Compute transformation matrix
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    
    # Apply transformation
    warped = cv2.warpPerspective(image, M, (image.shape[1], image.shape[0]))
    
    return warped

def detect_lines(image):
    """ """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 155, 255, cv2.THRESH_BINARY)[1]
    lines = cv2.HoughLinesP(gray, 1, np.pi / 180, 30, minLineLength=10, maxLineGap=30)
    lines = np.squeeze(lines) 
    return gray, lines


def tensor_to_tuples(tensor):
    """ Convert tensor to tuples """
    return [(tensor[i], tensor[i+1], tensor[i+2]) for i in range(0, len(tensor), 3)]