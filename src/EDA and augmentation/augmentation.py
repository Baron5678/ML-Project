import os
import cv2

# Function to split and merge images
def process_images(input_dir, output_dir):
    
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    j=0
    target_size = (128, 128)
    # Iterate through number directories in the initial set
    for number_dir in os.listdir(input_dir):
        files = os.listdir(os.path.join(input_dir, number_dir))
        input_number_dir = os.path.join(input_dir, number_dir)
        print(f"{j} directory")
        # Skip files, only process directories
        if not os.path.isdir(input_number_dir):
            continue

        # Create corresponding number directory in the eda_set folder
        output_number_dir = os.path.join(output_dir, number_dir)
        if not os.path.exists(output_number_dir):
            os.makedirs(output_number_dir)
        k=len(files)

        
        for i in range(len(files)):
            if i < len(files) - 3:
            
                img1 = cv2.imread(os.path.join(input_dir, number_dir, files[i]))

                img2 = cv2.imread(os.path.join(input_dir, number_dir, files[k-1]))

                img3 = cv2.imread(os.path.join(input_dir, number_dir, files[i+1]))

                img4 = cv2.imread(os.path.join(input_dir, number_dir, files[k-2]))

                desired_size = (128, 128)
                img1 = cv2.resize(img1, desired_size)
                img2 = cv2.resize(img2, desired_size)
                img3 = cv2.resize(img3, desired_size)
                img4 = cv2.resize(img4, desired_size)

                # Split images and merge halves
                height, width, _ = img1.shape
                half_width = width // 2
                half_height = height // 2

                combined_img = img1[:, :half_width]
                combined_img = cv2.hconcat([combined_img, img2[:, half_width:]])

                output_filename = f'fr_width_2_{os.path.basename(number_dir)}_{i}.jpg'
                output_path = os.path.join(output_number_dir, output_filename)
                cv2.imwrite(output_path, combined_img)

                combined_img = img1[:half_height, :]
                combined_img = cv2.vconcat([combined_img, img2[half_height:, :]])

                output_filename = f'fr_height_2_{os.path.basename(number_dir)}_{i}.jpg'
                output_path = os.path.join(output_number_dir, output_filename)
                cv2.imwrite(output_path, combined_img)

                quarter1 = img1[:half_height, :half_width]
                quarter2 = img2[:half_height, half_width:]
                quarter3 = img3[half_height:, :half_width]
                quarter4 = img4[half_height:, half_width:]   

                # Combine the quarters horizontally first
                top_half = cv2.hconcat([quarter1, quarter2])
                bottom_half = cv2.hconcat([quarter3, quarter4])

                # Then combine the halves vertically
                combined_img = cv2.vconcat([top_half, bottom_half]) 

                output_filename = f'fr_quarters_2_{os.path.basename(number_dir)}_{i}.jpg'
                output_path = os.path.join(output_number_dir, output_filename)
                cv2.imwrite(output_path, combined_img)

                k=k-1


        j=j+1


# Directory containing images
input_directory = './in'

# Output directory
output_directory = './out'
os.makedirs(output_directory, exist_ok=True)



# Process images based on the algorithm
process_images(input_directory, output_directory)

