import qrcode
from PIL import Image

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR code
data = "https://www.linkedin.com/in/milan-mehta-13393a2b8"  # Change this to your desired data
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Convert to RGB for color manipulation
img = img.convert("RGB")

# Apply color to the QR code (e.g., red)
pixels = img.load()
for i in range(img.size[0]):  # Width
    for j in range(img.size[1]):  # Height
        if pixels[i, j] == (0, 0, 0):  # If the pixel is black
            pixels[i, j] = (255, 0, 0)  # Change it to red

# Save the colored QR code
img.save("Milan_Mehta_Linkedin.png")
