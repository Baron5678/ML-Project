import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_average_color_transition(image):
    

    # Compute the gradient magnitude using Sobel operators
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Calculate the average gradient magnitude
    avg_gradient_magnitude = np.mean(gradient_magnitude)

    return avg_gradient_magnitude

def calculate_average_wrinkles(image):
    

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # Use the Canny edge detector
    edges = cv2.Canny(blurred, 30, 150)

    # Find contours in the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate total length of contours
    total_wrinkle_length = 0
    for contour in contours:
        total_wrinkle_length += cv2.arcLength(contour, True)

    return total_wrinkle_length

def visualize_color_and_wrinkles(eda_sized_set_folder):
    color_data = {}
    wrinkle_data = {}
    i=0
    for number_dir in sorted(os.listdir(eda_sized_set_folder), key=lambda x: int(x)):
        color_values = []
        wrinkle_values = []
        print(f"{i} directory")

        for filename in os.listdir(os.path.join(eda_sized_set_folder, number_dir)):
            image_path = os.path.join(eda_sized_set_folder, number_dir, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Calculate color transition
            avg_color_transition = calculate_average_color_transition(image)
            color_values.append(avg_color_transition)

            # Calculate wrinkles
            avg_wrinkles = calculate_average_wrinkles(image)
            wrinkle_values.append(avg_wrinkles)

        # Calculate the average color transition and wrinkles for the class
        avg_color = np.mean(color_values)
        avg_wrinkles = np.mean(wrinkle_values)

        color_data[number_dir] = avg_color
        wrinkle_data[number_dir] = avg_wrinkles
        i=i+1

    color_val = np.array(list(color_data.values()))
    histogram(color_val, 'Color transition')
    wrinkle_val = np.array(list(wrinkle_data.values()))
    histogram(wrinkle_val, 'Wrinkle frequency')


    # Plotting the features in separate windows
    # Plot Color Transition (Graph)
    plt.figure(figsize=(8, 6))
    plt.plot(color_data.keys(), color_data.values(), color='blue')
    plt.title('Average Color Transition (Graph)')
    plt.ylabel('Average Gradient Magnitude')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Plot Wrinkles (Graph)
    plt.figure(figsize=(8, 6))
    plt.plot(wrinkle_data.keys(), wrinkle_data.values(), color='red')
    plt.title('Average Wrinkles (Graph)')
    plt.ylabel('Average Wrinkle Length')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def histogram(data, string):
    scale = np.arange(111)

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.bar(scale, data)
    ax.set_title({string})

    plt.tight_layout()
    plt.show()


# Specify your "eda_sized_set" folder
eda_sized_set_folder = 'eda_set'

# Visualize color transition and wrinkles
visualize_color_and_wrinkles(eda_sized_set_folder)
