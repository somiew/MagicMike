# Python 3.8.7
import qrcode

def makeQR(data):
    qr = qrcode.QRCode(
        version=1,
        box_size=15,
        border=2
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('latestQR.png')