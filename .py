import easyocr
import PIL
from PIL import ImageDraw

# Initialize EasyOCR reader
reader = easyocr.Reader(["en"], gpu=False)

# Open the image
im = PIL.Image.open(r"C:\Users\User\Downloads\AI PROJECT\TestForAI.jpg")

# Perform OCR
bounds = reader.readtext(r'C:\Users\User\Downloads\AI PROJECT\TestForAI.jpg')

# Define function to draw bounding boxes
def draw_boxes(image, bounds, color='yellow', width=8):
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        p0, p1, p2, p3 = bound[0]
        draw.line([*p0, *p1, *p2, *p3, *p0], fill=color, width=width)
    return image

# Draw bounding boxes on the image
drawn_image = draw_boxes(im, bounds)

# Save the modified image with a different filename
drawn_image.save(r"C:\Users\User\Downloads\AI PROJECTnr_with_boxes.jpg")

# Print and write recognized text to a file
with open(r"C:\Users\User\Downloads\AI PROJECTnr_text.txt", mode='w', encoding="utf-8") as f:
    for i in bounds:
        print(i[1])
        f.write(i[1] + '\n')
