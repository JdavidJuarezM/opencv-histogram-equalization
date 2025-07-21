# -*- coding: utf-8 -*-
"""
Performs histogram equalization on an image to improve contrast.

This script uses OpenCV and Matplotlib to load an image, convert it to
grayscale, and then apply histogram equalization to enhance its contrast.
It saves the grayscale image, the equalized image, and the histograms
for both.

Dependencies:
    - opencv-python
    - matplotlib
    - numpy

Usage:
    1. Save this script in a folder.
    2. Place an input image named 'input_image.jpg' in the same folder.
    3. Run the script. All output files will be saved to a new
       'output/' subfolder.
"""
import cv2
import matplotlib.pyplot as plt
import os

# --- CONFIGURATION ---
INPUT_IMAGE_PATH = 'input_image.jpg'
OUTPUT_FOLDER = 'output'

# Create the output directory if it doesn't exist.
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)
    print(f"Created directory: {OUTPUT_FOLDER}")

# Verify the input image exists.
if not os.path.isfile(INPUT_IMAGE_PATH):
    print(f"Error: Input image not found at '{INPUT_IMAGE_PATH}'")
    exit()

# --- IMAGE PROCESSING ---
# 1. Load the original image.
original_image = cv2.imread(INPUT_IMAGE_PATH)

# 2. Convert the image to grayscale.
grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
cv2.imwrite(os.path.join(OUTPUT_FOLDER, 'grayscale_image.jpg'), grayscale_image)
print("Saved grayscale_image.jpg")

# 3. Generate and save the histogram for the grayscale image.
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.hist(grayscale_image.ravel(), bins=256, range=[0, 256])
plt.savefig(os.path.join(OUTPUT_FOLDER, 'grayscale_histogram.png'))
print("Saved grayscale_histogram.png")
# plt.show() # Uncomment to display plots during script execution

# 4. Equalize the grayscale image.
equalized_image = cv2.equalizeHist(grayscale_image)
cv2.imwrite(os.path.join(OUTPUT_FOLDER, 'equalized_image.jpg'), equalized_image)
print("Saved equalized_image.jpg")

# 5. Generate and save the histogram for the equalized image.
plt.figure()
plt.title("Equalized Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.hist(equalized_image.ravel(), bins=256, range=[0, 256])
plt.savefig(os.path.join(OUTPUT_FOLDER, 'equalized_histogram.png'))
print("Saved equalized_histogram.png")

print("\nProcessing complete. Check the 'output' folder.")
# plt.show() # Uncomment to display plots during script execution