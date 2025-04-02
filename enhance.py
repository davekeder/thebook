from PIL import Image
from PIL import ImageEnhance
import sys
import os

def enhance_image(image_path, output_dir):
    try:
        # Check if the input file exists
        if not os.path.exists(image_path):
            print(f"Error: {image_path} not found")
            return

        # Load the image
        img = Image.open(image_path)

        # Convert to grayscale
        img = img.convert("L")

        # Increase contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(3.0)  # Adjustable for handwriting

        # Create output filename in the output directory
        base_name = os.path.splitext(os.path.basename(image_path))[0]  # Get filename without path/extension
        output_path = os.path.join(output_dir, f"{base_name}_preprocessed.jpg")

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Save the enhanced image
        img.save(output_path)
        print(f"Enhanced {image_path} and saved as {output_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def process_folder(input_dir, output_dir):
    # Check if input directory exists
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist")
        return

    # Get all .jpg files in the input directory
    jpg_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.jpg')]

    if not jpg_files:
        print(f"No .jpg files found in {input_dir}")
        return

    # Process each file
    for jpg_file in jpg_files:
        input_path = os.path.join(input_dir, jpg_file)
        enhance_image(input_path, output_dir)

if __name__ == "__main__":
    # Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python enhance.py <input_subfolder> <output_subfolder>")
        print("Example: python enhance.py letters enhanced")
        sys.exit(1)

    # Get input and output subfolders from command line
    input_subfolder = sys.argv[1]
    output_subfolder = sys.argv[2]

    # Process all JPGs in the input subfolder
    process_folder(input_subfolder, output_subfolder)