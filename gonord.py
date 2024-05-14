from ImageGoNord import NordPaletteFile, GoNord

import os

def convert_images_in_folder(folder_path, output_folder):
    go_nord = GoNord()
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                image_path = os.path.join(root, file_name)
                output_path = os.path.join(output_folder, os.path.relpath(root, folder_path), file_name)
                output_folder_path = os.path.dirname(output_path)
                if not os.path.exists(output_folder_path):
                    os.makedirs(output_folder_path)
                try:
                    image = go_nord.open_image(image_path)
                    go_nord.convert_image(image, save_path=output_path)
                    print(f"Converted {image_path} to Nord palette and saved at {output_path}")
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

# Specify the folder containing images
input_folder = "Pictures/wallpapers"

# Specify the output folder
output_folder = "Pictures/nord-wallpapers"

convert_images_in_folder(input_folder, output_folder)
