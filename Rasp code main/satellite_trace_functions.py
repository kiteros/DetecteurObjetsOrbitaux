import math
import datetime
from satellite import Satellite, norm
import numpy as np
from analyse_pic_from_folder import read_img_name,read_img_times
from detect_position import time_from_str_to_datetime
import os

def get_saved_lines(filename):
    #DATAPATH='.\Processed\Lines\lines' + filename[:-4] + '_outputfinal.npy'
    #DATAPATH='Processed\Lines\lines' + filename[:-4] + '_outputfinal.npy'
    DATAPATH='Processed/Lines/lines' + filename[:-4] + '_outputfinal.npy'
    rhos=[]
    thetas=[]
    lines = np.load(DATAPATH)
    for i, line in enumerate(lines):
        for rho, theta in line:
            rhos.append(rho)
            thetas.append(theta)

    img_names = read_img_name("param_img.txt")
    img_times = read_img_times("param_img.txt")

    time=[]
    for i in range(0,len(img_names)):
        if img_names[i] == filename:
            for j in range(len(rhos)):
                time.append(img_times[i])


    #time=time_from_str_to_datetime(time)
    return rhos,thetas,time

def get_middles(filename):
    path = './Processed/Middles/' + filename[:-4] + '_output_Middles.npy'
    middles = np.load(path)
    middlesX = []
    middlesY = []
    for i, middle in enumerate(middles):
        middlesX.append(middle[0])
        middlesY.append(middle[1])

    return middlesX,middlesY

def data_for_el_from_folder(filenames):
    initial = 0
    for filename in filenames:
        (rhos, thetas, times) = get_saved_lines(filename)   # gsl to be written
        (middlesx,middlesy)=get_middles(filename) #to be written
        print('TIMES',times)
        if initial == 0:
            trace = (rhos[0], thetas[0], times[0])
            print('Test param trace: ',rhos[0],thetas[0],times[0])
            middle=(middlesx[0],middlesy[0])
        if len(rhos) > 0:
            sate1 = Satellite(trace,middle)
            satellites = [sate1]
            ++ initial
        for line_number in range(0,len(rhos)):
                for satellite in satellites:
                    trace = (rhos[line_number], thetas[line_number], times[line_number])
                    middle=(middlesx[line_number],middlesy[line_number])
                    known = True
                    if (isinstance(rhos[0],int)):
                        known = satellite.same_satellite(trace,middle)
                    if not(known):
                        new_sate = Satellite(trace,middle)
                        #new_sate
                        satellites.append(new_sate)
                        break   # useless to continue, no trace should correspond to 2 satellites
    return satellites




