import qrcode
from PIL import Image
import re
url_input = input("Enter a link : ")
pattern = re.search("((https?://)?(www\.)?)?[a-zA-Z0-9\-._]+\.[a-zA-Z]{2,3}", url_input)
if pattern:
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url_input)
    qr.make(fit=True)
    img = qr.make_image(fill_color="gold", back_color="black")
    img.save("QR.png")
    
    print("QR Code generated successfully.")
else:
    print("Invalid URL. Please enter a valid URL.")
