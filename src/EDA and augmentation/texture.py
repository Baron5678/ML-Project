import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.filters import gabor
from skimage import io, color, feature

def extract_texture_features_high(img):
    frequency = 0.6
    theta = 0
    gabor_response = gabor(img, frequency, theta=theta)
    return np.mean(gabor_response)

def extract_texture_features_low(img):
    frequency = 0.2
    theta = 0
    gabor_response = gabor(img, frequency, theta=theta)
    return np.mean(gabor_response)


def visualize_texture(eda_sized_set_folder):
    texture_data_high = {}
    texture_data_low = {}
    i=0
    for number_dir in sorted(os.listdir(eda_sized_set_folder), key=lambda x: int(x)):
        high_values = []
        low_values = []
        print(f"{i} directory")

        for filename in os.listdir(os.path.join(eda_sized_set_folder, number_dir)):
            image_path = os.path.join(eda_sized_set_folder, number_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            avg_high=extract_texture_features_high(image)
            high_values.append(avg_high)

            avg_low=extract_texture_features_low(image)
            low_values.append(avg_low)

        # Calculate the average color transition and wrinkles for the class
        avg_class_high = np.mean(high_values)
        avg_class_low = np.mean(low_values)

        texture_data_high[number_dir] = avg_class_high
        texture_data_low[number_dir] = avg_class_low
        i=i+1

    tex_high_scale = np.arange(111)
    tex_high_val = np.array(list(texture_data_high.values()))

    tex_low_scale = np.arange(111)
    tex_low_val = np.array(list(texture_data_low.values()))


    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 5))

    ax1.bar(tex_high_scale, tex_high_val)
    ax1.set_title('Texture high')

    ax2.bar(tex_low_scale, tex_low_val)
    ax2.set_title('Texture low')

    plt.tight_layout()
    plt.show()

    # Plotting the features in separate windows
    # Plot Color Transition (Graph)
    plt.figure(figsize=(8, 6))
    plt.plot(texture_data_high.keys(), texture_data_high.values(), color='blue')
    plt.title('Average Texture high')
    plt.ylabel('Average Texture high')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot Wrinkles (Graph)
    plt.figure(figsize=(8, 6))
    plt.plot(texture_data_low.keys(), texture_data_low.values(), color='red')
    plt.title('Average Texture low')
    plt.ylabel('Average Texture low')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()



# Specify your "eda_set" folder
eda_set_folder = 'eda_set'

# Visualize color transition and wrinkles
visualize_texture(eda_set_folder)
