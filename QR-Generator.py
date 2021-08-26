# Importing The QRCode Module
import cv2
import qrcode  # pip install qrcode

# ENCODING THE QRCODE

# Making The QRCode For URL
QRCodeImg = qrcode.make("https://github.com/praabindhp")

# Saving The QRCode Generted
QRCodeImg.save("Praabindh_GitHub.jpg")

# DECODING THE QRCODE

# Instantiating The QR DeCoder
QRDeCode = cv2.QRCodeDetector()

value, points, straight_qrcode = QRDeCode.detectAndDecode(cv2.imread("Praabindh_GitHub.jpg"))

# Print The Value After DeCoding
print(value)