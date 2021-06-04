import numpy as np
from PIL import Image
from utils.filtre import *

def get_raw_image(filename):
    DATAPATH='./Processed/ImgCompressed/'
    filename2=DATAPATH+filename
    raw_img = Image.open(filename)
    raw_img=filtre(raw_img)
    compressed_img=raw_img.resize((1200,800))
    compressed_img.save(filename2[:-4]+'compressed.jpg')

    raw_img = np.asarray(raw_img)
    rgb_weights = [0.2989, 0.5870, 0.1140]
    raw_img = np.dot(raw_img[...,:3],rgb_weights)
    return raw_img


