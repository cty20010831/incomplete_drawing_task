from PIL import Image
import os

def reshape_image(path, target_size = (400, 400)):
    """
    Resize + center-pad an image to exactly the target size (default: 400x400) 
    while preserving aspect ratio. Directly overwrite the current image 
    if its size does not match the target size. 
    """

    # Load and convert to grayscale (if not already)
    img = Image.open(path).convert("L")
    orig_w, orig_h = img.size

    assert (orig_w, orig_h) != target_size, "Image is already the target size."

    # Scale image to fit within 400x400
    scale = min(target_size[0] / orig_w, target_size[1] / orig_h)
    new_w, new_h = int(orig_w * scale), int(orig_h * scale)
    resized = img.resize((new_w, new_h), resample=Image.LANCZOS)

    # Create a white canvas
    canvas = Image.new("L", target_size, color=255)

    # Compute top-left corner to paste resized image
    x_offset = (target_size[0] - new_w) // 2
    y_offset = (target_size[1] - new_h) // 2

    canvas.paste(resized, (x_offset, y_offset))
    canvas.save(path)


def main():
    # Define the directory containing the images
    stimuli_dir = "public/images"

    # Reshape all incomplete shape stimuli
    for filename in os.listdir(stimuli_dir):
        if "Incomplete_Shape" in filename:
            image_path = os.path.join(stimuli_dir, filename)
            reshape_image(image_path)
            print(f"Resized {filename}.")


if __name__ == "__main__":
    main()