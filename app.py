from flask import Flask, request, render_template # pip install Flask
import pyzbar.pyzbar as pyzbar # pip install pyzbar
# Importing The QRCode Module
import cv2 # pip install opencv-python
import qrcode # pip install qrcode

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/upload/"

@app.route('/')
def home():
    return render_template('home.html')

# ENCODING THE QRCODE
@app.route('/encode')
def indexEn():
    return render_template('indexEn.html')

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

    value, points, straight_qrcode = QRDeCode.detectAndDecode(
        cv2.imread("static/QR_Image.jpg"))

    # Print The Value After DeCoding
    print(value)

    return render_template('qrcode.html')

@app.route('/decode')
def indexDe():
    return render_template('indexDe.html')

@app.route('/upload')
def upload_file():
    return render_template('indexDe.html')

@app.route('/decode', methods=['GET', 'POST'])
def save_file():
    if request.method == 'POST':
        f = request.files['file']
        # filename = secure_filename(f.filename)
        filename = "QR_EnCode.jpg"

        f.save(app.config['UPLOAD_FOLDER'] + filename)

    # DECODING THE QRCODE

    QRDeCode = pyzbar.decode(cv2.imread("static/upload/QR_EnCode.jpg"))
    value = QRDeCode[0].data.decode()

    # Displaying The Value After DeCoding
    return render_template('decode.html', value=value)

if __name__ == '__main__':
    app.run(debug=True)