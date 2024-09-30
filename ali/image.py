from PIL import Image
import io

def display(data:bytes) -> None:
    io_Img = io.BytesIO(data)
    image = Image.open(io_Img)
    image.show()