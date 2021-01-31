from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import Image


serial = spi(port=0, device=0, gpio=noop(), block_orientation=-90)
device = max7219(serial, width=8, height=32, rotate=1)


def display_image():
    img = Image.open("api_uploaded_files/test.png").convert("1")
    device.display(img)

def clear_display():
    pass

