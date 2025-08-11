import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"
new_size = (800, 600)  
output_format = "png"  # Change to 'jpg', 'bmp', 'gif', etc.

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)

        base_name = os.path.splitext(file_name)[0]
        output_path = os.path.join(output_folder, f"{base_name}_resized.{output_format}")

        if output_format.lower() in ['jpg', 'jpeg'] and img_resized.mode in ("RGBA", "P"):
            img_resized = img_resized.convert("RGB")

        img_resized.save(output_path, output_format.upper())
        print(f"Resized & converted: {output_path}")

print("All images resized and converted successfully!")
