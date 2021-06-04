from detect_position import time_middle
from utils.read_param import *
from altaz_to_IOD import *
import os

def creation_IOD_files(args, satellites):
    time, agvert, aghoriz, bouss, stnb, ststatut, texpos, focal, pixsize = read_param("parametres.txt")
    pscale = pixelscale(pixsize, focal)
    i=0
    nameIOD='IOD_sat_numero'
    print('LEN SATS ', len(satellites))
    for sat in satellites:
        i=i+1
        for i in range(0,len(sat.rhos)):
            t = time_middle(sat.times[i], texpos)
            px=sat.middlesx[i]
            py=sat.middlesy[i]
            [el, az] = positionAZEL(px, py, agvert, aghoriz, bouss, pscale)
            elstring = str(abs(int(el))).ljust(7, ' ')
            azstring = str(int(az)).ljust(7, ' ')
            sg = ""  # signe elevation
            if el > 0:
                sg = "+"
            else:
                sg = "-"
            fnameIOD = './Processed/IOD/'+nameIOD[:-4] + str(i) +'.txt'
            angleforme = "4"
            tuncert = "18"
            puncert = "18"
            objnb = "12345 98 123A  "

            conv_altaz_to_IOD(elstring, azstring, sg, angleforme, puncert, t, tuncert, objnb, stnb, ststatut, fnameIOD)



def Run_elfind_on_sats(pathelfind):
    '''
    os.system('ls')
    path='./Processed/IOD'
    path = path[2:len(path)]
    for fname in os.listdir(path):
        cmd = 'elfind ' + fname + '/'
        print(cmd)
        os.system(cmd)
    '''
    path = "./Processed/IOD"
    listnames = os.listdir(path)
    path3 = os.getcwd()
    os.chdir(pathelfind)
    for fname in listnames:
        fullname = path3 + '/Processed/IOD/' + fname
        print("Cannot run elfind.exe on Mac. Compile the cpp file in a Mac friendly way if needed.")
        #('elfind ' + fullname)