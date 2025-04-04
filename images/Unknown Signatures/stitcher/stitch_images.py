import os
import sys
from PIL import Image

def stitch_images_2x2(folder_path, output_path="stitched_output.png"):
    """
    Stitches four images from a folder into a 2x2 grid and saves the result.
    
    Args:
        folder_path (str): Path to the folder containing the images.
        output_path (str): Path to save the stitched image.
    """
    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        sys.exit(1)

    # Get list of image files in the folder (supporting common formats)
    image_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_extensions)]
    
    # Ensure exactly 4 images are present
    if len(image_files) != 4:
        print(f"Error: Expected exactly 4 images, but found {len(image_files)} in '{folder_path}'.")
        sys.exit(1)

    # Load the images
    images = []
    max_width = 0
    max_height = 0
    try:
        for img_file in image_files:
            img_path = os.path.join(folder_path, img_file)
            img = Image.open(img_path).convert("RGBA")  # Convert to RGBA for consistent handling
            images.append(img)
            # Track the maximum width and height to preserve resolution
            max_width = max(max_width, img.width)
            max_height = max(max_height, img.height)
    except Exception as e:
        print(f"Error loading images: {e}")
        sys.exit(1)

    # Calculate the dimensions of the final 2x2 grid
    # Each cell in the grid will be the size of the largest image
    grid_width = max_width * 2
    grid_height = max_height * 2

    # Create a new blank image for the 2x2 grid with a white background
    stitched_image = Image.new("RGBA", (grid_width, grid_height), (255, 255, 255, 255))

    # Place each image in the 2x2 grid
    positions = [
        (0, 0),              # Top-left
        (max_width, 0),      # Top-right
        (0, max_height),     # Bottom-left
        (max_width, max_height)  # Bottom-right
    ]

    for i, (img, pos) in enumerate(zip(images, positions)):
        # Center the image in its grid cell if it's smaller than the max size
        x_offset = pos[0] + (max_width - img.width) // 2
        y_offset = pos[1] + (max_height - img.height) // 2
        stitched_image.paste(img, (x_offset, y_offset))

    # Save the stitched image
    try:
        stitched_image.save(output_path, "PNG")
        print(f"Stitched image saved as '{output_path}'.")
    except Exception as e:
        print(f"Error saving stitched image: {e}")
        sys.exit(1)

    # Close all images to free memory
    for img in images:
        img.close()
    stitched_image.close()

if __name__ == "__main__":
    # Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    # Get the folder path from command-line argument
    folder_path = sys.argv[1]
    
    # Call the stitching function
    stitch_images_2x2(folder_path)