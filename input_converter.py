import PIL
from PIL import Image, ImageFilter
from numpy import array
import numpy as np

def convert():
    img = Image.open('C:/python_files/saved_images/image.png')
    #img = img.crop((0, 0, 10, 10))
    for i in range(2): img = img.filter(ImageFilter.SMOOTH)
    img = img.convert('L').resize((28, 28), PIL.Image.NEAREST) # convert image to 8-bit grayscale
    img.save('C:/python_files/saved_images/image.png')
    WIDTH, HEIGHT = img.size
    
    data = list(img.getdata()) # convert image data to a list of integers
    # convert that to 2D list (list of lists of integers)
    inverted_data = []
    for pixel in data:
        pixel =  (pixel - 255) * (-1)
        inverted_data.append(pixel)

    greyscale_matrix = np.asarray(inverted_data).reshape((28, 28))
    return greyscale_matrix
