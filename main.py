import os
import pyqrcode 
from PIL import Image

class QR Gen(object); def_init__(self, text):

self.gr_image= self.gr generator (text)

staticmethod

def qr generator (text): qr code pyqrcode.create (text)

file name "QR Code Result"

save_path = os.path.join(os.path.expanduser(''), 'Desktop")

name = f*{save_path}{file_name].png"

qr_code.png(name, scale-18)

image Image.open(name)

image image.resize((400,400), Image ANTIALIAS)

image.show()

if name main": 08 Gen (input("[QR] Enter text or link: "))
