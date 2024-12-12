import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def age_hist(input_folder):
    i = 0
    arr = np.zeros(117, dtype=int)
    # Iterate through number directories in the input folder (eda_set)
    for number_dir in sorted(os.listdir(input_folder), key=lambda x: int(x)):
        input_number_dir = os.path.join(input_folder, number_dir)

        # Skip files, only process directories
        if not os.path.isdir(input_number_dir):
            continue

        l = len(os.listdir(input_number_dir))
        print(f"{i} directory: {l} files")
        arr[i] = l
        i = i + 1

    print(np.sum(arr))
    fig = plt.figure(figsize=(10, 5))
    plt.bar(np.arange(117), arr)
    plt.title("age distribution")
    plt.show()


eda_set_folder = 'eda_set'
age_hist(eda_set_folder)
