from PIL import Image
import os

def crop_header(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        width, height = img.size
        pixels = img.load()

        print(f"Processing {image_path} ({width}x{height})")

        # Find the first non-white row (top of text)
        first_content_row = 0
        for y in range(height):
            row_has_content = False
            for x in range(width):
                r, g, b, a = pixels[x, y]
                # Check if pixel is not white (assuming white background)
                if (r < 250 or g < 250 or b < 250) and a > 0:
                    row_has_content = True
                    break
            if row_has_content:
                first_content_row = y
                break
        
        print(f"First content row (text top): {first_content_row}")

        # Find the next white row (bottom of text)
        text_bottom_row = first_content_row
        for y in range(first_content_row, height):
            row_is_white = True
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if (r < 250 or g < 250 or b < 250) and a > 0:
                    row_is_white = False
                    break
            if row_is_white:
                text_bottom_row = y
                break
        
        print(f"Text bottom row: {text_bottom_row}")

        # Find the next non-white row (top of diagram)
        diagram_top_row = text_bottom_row
        for y in range(text_bottom_row, height):
            row_has_content = False
            for x in range(width):
                r, g, b, a = pixels[x, y]
                if (r < 250 or g < 250 or b < 250) and a > 0:
                    row_has_content = True
                    break
            if row_has_content:
                diagram_top_row = y
                break
        
        print(f"Diagram top row: {diagram_top_row}")

        # Crop
        # Add a small buffer above the diagram if needed, or just crop exactly
        crop_y = max(0, diagram_top_row - 10) # 10px padding
        
        # Check if we actually found a gap
        if crop_y <= first_content_row:
             print("Warning: Could not distinguish text from diagram. Skipping crop.")
             return

        cropped_img = img.crop((0, crop_y, width, height))
        cropped_img.save(image_path)
        print(f"Successfully cropped {image_path}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

base_dir = r"c:\Users\geraw\provengo-seminar\public\slides_images"
images = ["online_store_login.png", "online_store_add_to_cart.png"]

for img_name in images:
    crop_header(os.path.join(base_dir, img_name))
