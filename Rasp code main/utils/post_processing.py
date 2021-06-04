import numpy as np
import cv2
import math
import networkx as nx
from utils.lines import *

palette = [(255,0,0),(0,255,0),(255,255,0),(255,0,255),(0,255,255)] #red, green, yellow, majenta, cyan

def distinguish_satellites(h,w, h_results, threshold = 200000.):
    """
    from all lines detected by hough, retrieve one line per streak in the image
    Parameters
    ----------
    h : int
    w : int
    h_results : list
        (rho, theta) parameters of all lines detected by hough
    id_: tuple(int)
        coordinates of the block in the (4,8) matrix defining the mosaic
    threshold : float
        threshold value to create an edge in the adjacency matrix
    Return
    ----------
    result : list
        (rho, theta) parameters defining a line per streak
    """
    if h_results is not None and len(h_results) > 0:
        #print(h_results, h_results.shape)
        filtered_lines = h_results
        n = len(filtered_lines)
        m_lines = []
        for i, line in enumerate(filtered_lines):
            for rho, theta in line :
                if theta != 0 :
                    (x0,y0), b, a = get_slope_parameters(rho, theta)
                    F = lambda x : (a*(x**2))/2 + b*x
                    m_lines.append(F(w-1) - F(0))
                #else:
                    #print('vertical line !!! (%d,)') #detect if we had false positives in our dataset (no streak were vertical)
        dist_mat = np.zeros((n,n)) #,dtype='uint8'
        for i,x in enumerate(m_lines) :
            for j,y in enumerate(m_lines):
                dist_mat[i,j] = abs(x - y)
        adj_mat = (dist_mat < threshold).astype(float) - np.eye(dist_mat.shape[0])
        G = nx.from_numpy_matrix(adj_mat)
        #print("Number of satellites : %d" % nx.number_connected_components(G)) #one connected components corresponds to a streak
        return [np.median(filtered_lines[list(c)], axis = 0) for c in sorted(nx.connected_components(G), key=len, reverse=True)]
    return []

def get_window_from_line(img, line, theta_step = 0.1*math.pi/180., theta_midrange = 10, axis_midrange = 30):
    h, w = img.shape
    for rho, theta in line:
        final_j = np.arange(-theta_midrange,theta_midrange+1)
        result_band = np.arange(-axis_midrange, axis_midrange)
        return rho, line[0][1] + theta_step * final_j, result_band
    # return rho,

def get_satellites_blocs(img, h_result):
    rs = []
    ts = []
    bs = []
    h,w = img.shape
    lines = distinguish_satellites(h, w, h_result) # must distinguish satellites
    #lines = h_result
    for i, line in enumerate(lines):
        r,t,b= get_window_from_line(img, line, theta_step = 0.05*math.pi/180., theta_midrange = 2, axis_midrange = 5)
        if b is not None:
            rs.append(r)
            ts.append(t)
            bs.append(b)
    return lines, rs, ts, bs

def retrieve_raw_satellites(crop, h_result):

    filterSize = (30, 30)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, filterSize)
    tophat_img = cv2.morphologyEx(crop, cv2.MORPH_TOPHAT, kernel)
    (retVal, img_gseuil) = cv2.threshold(tophat_img, 120, 1., cv2.THRESH_BINARY)
    th_crop = np.multiply(crop, img_gseuil)
    lines, rs, ts, bs = get_satellites_blocs(th_crop, h_result)
    h,w = th_crop.shape
    new = np.zeros((h,w,3)).astype(int) + crop.reshape(h,w,1).astype(int)
    #rho = rs[int(len(rs)/2)]
    #theta = ts[int(len(ts)/2)][int(len(ts)/2)]
    #bresen_line = build_line(rho, theta, 100, h, w)
    #new[bresen_line[:, 0], bresen_line[:, 1]] = palette[1 % 5]
    for i, r in enumerate(rs):
        for j in bs[i]:
            bresen_line = build_line(r, ts[i], j, h,w)
            new[bresen_line[:,0], bresen_line[:,1]] = palette[i%5] #nouvelle image avec les lignes dessinées dessus
    return new, (lines, rs,ts,bs) # ici les lines retournées sont les lines apres avoir enlevé les lignes multiples
# new : nouvelle image avec lignes