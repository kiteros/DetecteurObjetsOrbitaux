import os
import math
import time
import cv2
import numpy as np
from utils.canny import cannyEdgeDetector
from utils.post_processing import *

def process_block(params):  # partie technique importante du traitement de la matrice


    crop, h_threshold, filename, load_lines, save_lines = params

    hough_results = [None]*8
    if load_lines and os.path.exists(filename):
        lines = np.load(filename, allow_pickle = True)
        hough_results[-1] = lines
    else:
        #print('Start Hough Processing')
        start = time.time()
    sortie = crop # car on ne fait pas beaucoup des étapes intermédiaires nécessaires sur les .fit

    h,w = sortie.shape
    detector = cannyEdgeDetector([sortie], sigma=1.4, kernel_size=5, lowthreshold=0.09, highthreshold=0.17, weak_pixel=100)
    gauss, nonmax, th, imgs_final = detector.detect()
    lines = cv2.HoughLines(np.uint8(imgs_final[0]), 1, np.pi / 180, h_threshold)
    end = time.time()
    seconds = (end-start)
    #print('... Ending Hough Processing after %d min %d sec' % tuple([seconds // 60, seconds % 60]))
    #print('Nb of lines',len(lines))
    #print('SAVING LINES')
    if save_lines :
        if lines is None :
            lines = np.array([])
        np.save(filename, lines)
    #ici saving lines
    #print('Start Post-Processing...')
    start = time.time()
    new, final_results = retrieve_raw_satellites(crop, lines)
    end = time.time()
    seconds = (end-start)
    #print('... Ending Post-Processing after %d min %d sec' % tuple([seconds // 60, seconds % 60]))

    return tuple(hough_results), final_results, new # dans finalresults il y a les lignes simples, new : nvlle image avec lignes







