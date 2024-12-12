import os
import cv2

def process_images(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    i=0
    target_size = (128, 128)
    # Iterate through number directories in the initial set
    for number_dir in os.listdir(input_folder):
        input_number_dir = os.path.join(input_folder, number_dir)
        print(f"{i} directory")
        # Skip files, only process directories
        if not os.path.isdir(input_number_dir):
            continue

        # Create corresponding number directory in the eda_set folder
        output_number_dir = os.path.join(output_folder, number_dir)
        if not os.path.exists(output_number_dir):
            os.makedirs(output_number_dir)

        # Process each image in the number directory
        for filename in os.listdir(input_number_dir):
            input_path = os.path.join(input_number_dir, filename)

            # Load the image
            img = cv2.imread(input_path)

            # Resize the image to the target size
            img = cv2.resize(img, target_size)

            # Convert to black and white
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            
            # Save the processed image to the eda_set folder
            output_path = os.path.join(output_number_dir, filename)
            cv2.imwrite(output_path, gray)
        i=i+1




# Specify your input and output folders
input_folder = './in'
output_folder = './out'

# Process the images and create the visualization
process_images(input_folder, output_folder)
