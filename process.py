import os
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import imageio

def generate_sketch(input_path, output_dir, sigma=3, threshold=5, black_threshold=190):
    """
    Process an image to generate a sketch effect and save it to the specified directory.
    
    Parameters:
        input_path (str): Path to the input image.
        output_dir (str): Directory where the output sketch will be saved.
        sigma (float): Sigma for Gaussian smoothing. Default is 2.
        threshold (float): Threshold for edge detection. Default is 50.
        black_threshold (float): Threshold for turning shades of grey to black. Default is 200.
    """
    # Load the image
    image = imageio.imread(input_path, mode='F')
    # Apply Gaussian filter with specified sigma for smoothing
    smoothed_image = ndimage.gaussian_filter(image, sigma=sigma)
    # Apply Sobel filter in both x and y directions, and combine
    sobel_combined = np.hypot(ndimage.sobel(smoothed_image, axis=0), ndimage.sobel(smoothed_image, axis=1))
    # Apply a threshold to enhance edges (you can adjust the threshold value)
    sobel_combined[sobel_combined < threshold] = 0
    # Invert the image to get a sketch effect
    sketch = 255 - sobel_combined  # Inverting the colors
    # Turn shades of grey past the black_threshold to black
    sketch[sketch < black_threshold] = 0
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)  
    # Create the output file path with a unique identifier
    base_name = os.path.basename(input_path).replace('.jpg', '')
    output_path = os.path.join(output_dir, f"{base_name}_sketch.jpg")
    # Save the sketch as an image
    plt.imsave(output_path, sketch, cmap='gray')
    print(f"Sketch saved to {output_path}")

def process_directory(input_dir, output_dir, sigma=2.5, threshold=60, black_threshold=200):
    """
    Process all images in the input directory to generate sketches and save them to the output directory.
    
    Parameters:
        input_dir (str): Directory containing input images.
        output_dir (str): Directory where the output sketches will be saved.
        sigma (float): Sigma for Gaussian smoothing. Default is 23.
        threshold (float): Threshold for edge detection. Default is 5.
        black_threshold (float): Threshold for turning shades of grey to black. Default is 190.
    """
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg'):
            input_path = os.path.join(input_dir, filename)
            generate_sketch(input_path, output_dir, sigma, threshold, black_threshold)

# Example usage
process_directory('dog_images/n02085620-Chihuahua', 'output_sketches')


