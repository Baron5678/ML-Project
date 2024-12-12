import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_gray_pixels(input_folder):
    gray_pixels = np.zeros(256)

    i = 0
    # Iterate through number directories in the input folder (eda_set)
    for number_dir in os.listdir(input_folder):
        input_number_dir = os.path.join(input_folder, number_dir)
        print(f"{i} directory")
        # Skip files, only process directories
        if not os.path.isdir(input_number_dir):
            continue

        # Process each image in the number directory
        for filename in os.listdir(input_number_dir):
            input_path = os.path.join(input_number_dir, filename)

            # Load the image
            img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
            blur = cv2.GaussianBlur(img, (5,5), 0)
            unique, counts = np.unique(blur, return_counts=True)
            gray_pixels[unique] += counts

        i = i+1

    return gray_pixels


def gray_histogram(young_gray_pixels, old_gray_pixels):
    y_gray_scale = np.arange(256)
    y_normalised = young_gray_pixels / np.sum(young_gray_pixels)

    o_gray_scale = np.arange(256)
    o_normalised = old_gray_pixels / np.sum(old_gray_pixels)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))

    ax1.bar(y_gray_scale, y_normalised)
    ax1.set_title('Young gray blurred frequency')

    ax2.bar(o_gray_scale, o_normalised)
    ax2.set_title('Old gray blurred frequency')

    plt.tight_layout()
    plt.show()


young_folder = 'young_set'
young_gray_pixels = get_gray_pixels(young_folder)
old_folder = 'old_set'
old_gray_pixels = get_gray_pixels(old_folder)
gray_histogram(young_gray_pixels, old_gray_pixels)

