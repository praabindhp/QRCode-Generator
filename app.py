from flask import Flask
from flask import Flask, request, render_template

# Importing The QRCode Module
import cv2
import qrcode  # pip install qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# ENCODING THE QRCODE
@app.route('/qrcode', methods=["GET", "POST"])
def decode():
    value = request.form.get("value")

    # Making The QRCode For URL
    QRCodeImg = qrcode.make(value)

    # Saving The QRCode Generted
    QRCodeImg.save("static/QR_Image.jpg")

    # DECODING THE QRCODE

    # Instantiating The QR DeCoder
    QRDeCode = cv2.QRCodeDetector()

    value, points, straight_qrcode = QRDeCode.detectAndDecode(cv2.imread("static/QR_Image.jpg"))

    # Print The Value After DeCoding
    print(value)

    return render_template('qrcode.html')

if __name__ == '__main__':
    app.run(debug=True)