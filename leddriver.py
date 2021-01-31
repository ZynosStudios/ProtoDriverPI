from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image


serial = spi(port=0, device=0, gpio=noop(), block_orientation=-90)
device = max7219(serial, width=32, height=8)

img = Image.open("api_uploaded_files/test.png")

def display_image():
    with canvas(device) as draw:
        draw.draw(img)

def clear_display():
    pass

