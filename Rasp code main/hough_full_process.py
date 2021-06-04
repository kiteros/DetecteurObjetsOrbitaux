from matplotlib import pyplot as plt
import time
import os
import numpy as np

import utils.prologue as prologue
from utils.mosaic import *
from utils.img_processing import process_block


def houghfull(args,inputname,outputname): #sappelait main avant
    DATAPATH = './Processed/Lines/lines'
    global_start = time.time()
    raw_img = get_raw_image(inputname) # converti en array
    filename = DATAPATH + outputname[:-4] + '.npy' # nomme le fichier de sortie
    dict_lines = process_block((raw_img, args.hough, filename, args.load_lines, args.save_lines)) # process l'image
    global_end = time.time()
    seconds = (global_end - global_start)
    #print('... Ending Full Processing after %d min %d sec' % (seconds // 60, seconds % 60))

    #f, axes = plt.subplots(1,1)
    DATAPATH2='./Processed/ImgLines/'
    outputname2=DATAPATH2+outputname
    _, final, crop_img = dict_lines
    im = Image.fromarray((crop_img).astype(np.uint8))
    im.save(outputname2)

    #axes.imshow(crop_img)
    #plt.savefig(outputname)
    # final = (lines, rs,ts,bs) avec lines les nvlles lines qu'on veut extraire
    linesfin, rs, ts, bs = final
    filename2 = DATAPATH + outputname[:-4] + 'final.npy'  # nomme le fichier de sortie
    np.save(filename2, linesfin)

#if __name__ == '__main__':
    #main(prologue.get_args())

