import numpy as np
import os
from altaz_to_IOD import *
import utils.prologue as prologue
from utils.mosaic import *
from hough_full_process import *
from detect_position import *
from utils.read_param import *
from utils.save_img_zentren import *
import matplotlib.image as mpimg


def process_one_img(args, inputname,outputname):

    #---------Lecture Parametres--------------------------

   # agvert, aghoriz, bouss, stnb, ststatut, texpos, focal, pixsize=read_param("parametres.txt")

    # --------Hough_full_process---------------------------
    houghfull(args, inputname,outputname)

    #----------Position_Sat-------------------------------------
    DATAPATH = './Processed/Lines/lines'
    filenamelines = DATAPATH + outputname[:-4] + 'final.npy'
    inputname2='./Processed/ImgCompressed/'+inputname[:-4]+'compressed.jpg'
    Middles,Sets = position(inputname2,filenamelines)

    #----------Save_Image_with_lines+points----------------------

    save_img_zentren(inputname2, outputname, Middles, Sets)

    '''
    #----------Time---------------------------------------------
    t=time_middle(date,texpos)

    #----------Conversion position pixels-----------------------
    pscale = pixelscale(pixsize,focal)
    [el, az] = positionAZEL(px, py, agvert, aghoriz, bouss, pscale)
    elstring = str(abs(int(el))).ljust(7, ' ')
    azstring = str(int(az)).ljust(7, ' ')
    sg = "" #signe elevation
    if el > 0:
        sg = "+"
    else:
        sg = "-"
    #---------Ecriture fichier IOD------------------------------
    fnameIOD=nameIOD
    angleforme = "4"
    tuncert = "18"
    puncert = "18"
    objnb = "12345 98 123A  "

    conv_altaz_to_IOD(elstring, azstring, sg, angleforme, puncert, t, tuncert, objnb, stnb, ststatut, fnameIOD)

    #---------ELFIND-------------------------------------------
    
    cmd = 'elfind ' + fnameIOD
    os.system(cmd)
    '''


#if __name__ == '__main__':
 #   main(prologue.get_args())

