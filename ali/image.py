from PIL import Image
from io import BytesIO

def display(data:BytesIO) -> None:
    image = Image.open(data)
    image.show()