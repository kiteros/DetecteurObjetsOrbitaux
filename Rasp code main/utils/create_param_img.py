import os
from datetime import datetime

#   Contains functions to create param_img from the name of the folder containing all the images

def create_param_img(time, foldername): #time=real time ?
    param_img = open("param_img.txt","w+")
    #filenames = os.listdir(foldername)
    foldername = '../TEST'  #
    filenames = [f for f in os.listdir(foldername) if f.endswith('.jpg')]
    rasp_times = []
    for filename in  filenames:
        #if filename != "parametres.txt" and filename != "param_img.txt":
        rasp_times.append((get_rasp_time(filename)))
    delta = time - min(rasp_times)
    for j in range(0,len(rasp_times)):
        rasp_times[j] = rasp_times[j] + delta
        time_string = rasp_times[j].strftime("%Y%m%d%H%M%S%f")
        param_img.write(filenames[j] + "    " + time_string + '\n')
    param_img.close()

def get_rasp_time(filename):
    time = datetime(int(filename[4:8]),int(filename[9:11]),int(filename[12:14]),int(filename[15:17]),int(filename[18:20]),int(filename[21:23]),int(filename[25:29]+'000'))
    return time





