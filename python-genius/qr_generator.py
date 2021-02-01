import io
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter


def qr_generator():

    #option 1 print to a file-like object:
    rv = io.BytesIO()
    EAN13('123581321340', writer=ImageWriter()).write(rv)
    image = Image.open(rv)
    image = image.resize((400,400), Image.ANTIALIAS)
    image.show()

    # option 2, to an actual file:
    with open('QR-generator.jpeg', 'wb') as f:
        EAN13('123581321340', writer=ImageWriter()).write(f)

if __name__ == '__main__':
    qr_generator()
