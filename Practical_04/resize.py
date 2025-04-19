from PIL import Image
import os

# Input and output paths
input_path = 'images/input.jpg'
output_path = 'output/resized.jpg'

# Open image
img = Image.open(input_path)

# Reduce resolution (example: 25% of original)
new_size = (img.width // 4, img.height // 4)
resized_img = img.resize(new_size)

# Save the reduced image
os.makedirs(os.path.dirname(output_path), exist_ok=True)
resized_img.save(output_path)

print(f"Image resized to {new_size} and saved to {output_path}")
