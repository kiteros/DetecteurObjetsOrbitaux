from bresenham import bresenham
from matplotlib import numpy as np
from datetime import datetime, timedelta
from utils.mosaic import *
from utils.post_processing import *
import numpy as np

import matplotlib.image as mpimg
import argparse
import statistics as st

# input: rho, theta, image(as matrix already)
# output: chosen point belonging to the line
'''
parser = argparse.ArgumentParser(description='Trace in lines')
parser.add_argument('--i',type=str)
parser.add_argument('--l',type=str)
args = parser.parse_args()
'''

#def get_args():
 #   return args

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def get_points(rho, theta):
    """
    Generate points belonging to the line with (rho, theta) parameters

    Parameters
    ----------
    rho : float
    theta : float
        radian
    Return
    ----------
    (x0,y0),(x2,y2),(x2,y2): tuple(float), tuple(float), tuple(float)
        x,y coordinates of 3 points belonging to the (rho, theta) line
    """
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 10000 * (-b)) #   10000 chosen sufficiently large, dependeing on image size
    y1 = int(y0 + 10000 * (a))
    x2 = int(x0 - 10000 * (-b))
    y2 = int(y0 - 10000 * (a))
    return (x1,y1),(x2,y2)

def position(input,filelines):
    #   internal parameters
    threshold = 0.075 # experimental parameter
    #   get parameters
    img = mpimg.imread(input)
    img = img / np.max(img)
    '''
    filename_lines = args.l
    lines = np.load(filename_lines)
   '''
    #img=get_raw_image(args.i)
    # rho = lines[0][0][0]
    # theta = lines[0][0][1]  # apply the algorithm to the first line only at the moment
    #   apply filter to the image?
    #   get 2 points to use bresenham
    Middles=[]
    Traces=[]
    lines=np.load(filelines)
    for i, line in enumerate(lines):
        for rho, theta in line:
            point1, point2 = get_points(rho, theta)
            x1, y1 = point1
            x2, y2 = point2
            #   define set of points potentially belonging to the trace
            xdim = len(img[:])
            ydim = len(img[0][:])
            # set = list(bresenham(x1,y1,x2,y2))
            set = build_line(int(rho/5), theta, 0, xdim, ydim)
            #   reduce dimensions so that the points correspond to a pixel
            clean_set = []

            for point in set:  # first conversio, hasardeous. Maybe need to shift the origin (denke ich so)
                if (0 <= point[0] < xdim):
                    if (0 <= point[1] < ydim):
                        clean_set.append(point)
            set = clean_set
            #   initialize trace
            trace = []
            #   check whether each point in the set is in the trace (sufficiently bright in the relevant norm)
            a = 4  # length of interval
            length = len(set)

            XX = []
            YY = []
            for ind in range(0, length):
                XX.append(set[ind][0])
                YY.append(set[ind][1])

            # print('set',list(set))
            for idx in range(0, length):
                point = set[idx]
                vector = []
                x = point[0]
                y = point[1]
                for i in range(-a, a):
                    for j in range(-a, a):
                        if ((x + i in XX) and (y + j in YY)):
                            vector.append(img[x + i][y + j])
                sum = np.mean(vector)
                #print(sum)

                if sum > threshold:
                    trace.append(point)

            #   trace contains points in the trace
            # print('Trace=', trace)
            # middle = trace[int(len(trace)/2)]   #   get average point in the trace (rounded)
            x_compo = []
            y_compo = []
            for ind in range(0, len(trace)):
                x_compo.append(trace[ind][0])
                y_compo.append(trace[ind][1])


            mean_x=0
            mean_y=0
            if len(x_compo) !=0:
                mean_x = np.mean(x_compo)
            if len(y_compo) !=0:
                mean_y = np.mean(y_compo)

            middle = (int(mean_x), int(mean_y))

            Middles.append(middle)
            Traces.append(trace)


    return Middles, Traces

def time_from_str_to_datetime(date):
    date = date + '000'
    t = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]), int(date[8:10]), int(date[10:12]), int(date[12:14]),
                 int(date[14:20]))
    return t

def time_from_datetime_to_str(t):
    date=t.strftime("%Y%m%d%H%M%S%f")
    date=date[:-3]
    return date

def time_middle(date,timeexpos):
    #date=string YYYYMMDDHHMMSSsss, timeexpos in seconds
    t=time_from_str_to_datetime(date)
    delta=timedelta(seconds=timeexpos/2)
    tnew=t+delta
    tmid=time_from_datetime_to_str(tnew)
    return tmid

