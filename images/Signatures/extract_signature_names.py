import os

# Specify the folder path where the signature images are stored
folder_path = "."  # Replace with your folder path

# Specify the output text file path
output_file = "signature_names.txt"

# List to store the extracted names
names = []

# Get all .jpg files in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".jpg"):
        # Remove the .jpg extension and split the filename on underscores
        name_parts = filename[:-4].split("_")
        # Join the parts with spaces to form the full name
        full_name = " ".join(name_parts)
        names.append(full_name)

# Sort the names alphabetically for better readability
names.sort()

# Write the names to the output text file
with open(output_file, "w") as f:
    for name in names:
        f.write(name + "\n")

print(f"Extracted {len(names)} names and wrote them to {output_file}")