import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def save_img_zentren(inputname2, outputname, Middles,Sets):

    palette = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 255),
               (0, 255, 255)]  # red, green, yellow, majenta, cyan

    DATAPATH1='./Processed/Middles/'
    DATAPATH2='./Processed/Sets/'
    DATAPATH3='./Processed/ImgCenter/'

    imlines = Image.open(inputname2)
    imlines = np.asarray(imlines)
    rgb_weights = [0.2989, 0.5870, 0.1140]
    imlines = np.dot(imlines[..., :3], rgb_weights)

    h, w = imlines.shape
    new = np.zeros((h, w, 3)).astype(int) + imlines.reshape(h, w, 1).astype(int)

    N=len(Middles)
    for i in range(0,N):
        middle=Middles[i]
        set=Sets[i]
        px=middle[0]
        py=middle[1]

        b=2
        b2=4


        length = len(set)
        for i in range(0, length):
            coord = set[i]
            coord1 = coord[0]
            coord2 = coord[1]
            for i in range(-b,b):
                for j in range(-b, b):
                    if (coord1 + i >= 0) and (coord1 + i < w) and (coord2 + i >= 0) and (coord2 + i < h):
                        new[coord1 + i, coord2 + j] = palette[3]
            # new[coord1, coord2] = palette[1]

        for i in range(-b2, b2):
            for j in range(-b2, b2):
                if (px + i>=0) and (px + i<w) and(py + i>=0) and (py + i<h):
                    new[px + i, py + j] = palette[2]



    filenamepoints = DATAPATH3 + outputname[:-4] + '_points.jpg'
    #f, axes = plt.subplots(1, 1, figsize=(64, 64))

    im = Image.fromarray((new).astype(np.uint8))
    im.save(filenamepoints)

    np.save( DATAPATH1+outputname[:-4]+ '_Middles', Middles)
    np.save(DATAPATH2+outputname[:-4]+ '_Sets', Sets)
