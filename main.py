from PIL import Image
from pyzbar.pyzbar import decode

# Load image using Pillow
image_path = "google.jpeg"
img = Image.open(image_path)

# Decode all barcodes/QR codes found in the image
decoded_objects = decode(img)

for obj in decoded_objects:
    print("Type:", obj.type)                         # e.g., 'QRCODE', 'EAN13', 'CODE128'
    print("Data:", obj.data.decode("utf-8"))        # Raw decoded string
    print("Bounding Box:", obj.rect)                # Rect(left, top, width, height)
    print("Polygon Points:", obj.polygon)           # Corners for precise overlay