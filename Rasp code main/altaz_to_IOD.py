import math
import os

def pixelscale (pixelsize=5.97, focal=35):
    # computes the pixelscale i.e. the angular width and height of a pixel
    # arguments : pixelsize: in microns, focal:  telescope focal length in mm
    # outputs : pixelscale in arcseconds
    # see http://cbellh47.blogspot.com/2010/01/astrometry-101-pixel-scale.html
    return 206.265*pixelsize/focal

def positionAZEL (pixelx, pixely, anglevert, anglehoriz, boussole, pixscale):
    # calcule la position du pixel dans le systeme de coordonnées alt-az
    # renvoie les angles en arcsec: h=elevation, A=azimuth
    # anglevert, anglehoriz : radians, angles d'inclinaison de la caméra
    # boussole : radians, angle entre le nord et l'orientation de la camera
    # pixscale : en arcsec
    h=anglevert*206265+(pixely*math.cos(anglehoriz)-pixelx*math.sin(anglehoriz))*pixscale
    A=boussole*206265+(pixelx*math.cos(anglehoriz)+pixely*math.sin(anglehoriz))*pixscale

    return(h,A)

def conv_altaz_to_IOD(h,A,signe,angleform,posuncert, date,timeuncert, objectnumber, stationnumber, stationstatut, filename):

    # ecrit les donnes sous le format IOD et les enregistre dans un fichier txt
    os.system('ls')
    filename = filename[2:len(filename)]
    File = open(filename, "w")
    str1= objectnumber + " " + stationnumber + " " + stationstatut + " " + date + " " + timeuncert + " " + angleform \
    + " " + " " + A + signe + h + " " + posuncert + "                "
    File.write(str1)
    File.write("\n")
    File.close()



'''
################### CODE TEST #############################################

################### Données caméra ########################################

focal = 35 #mm , notee sur objectif
pixsize = 5.97 #micron calculee a partir de la taille du capteur (35.8mm x 23.9mm) divisé par nb de pixel (6000 x 4000)

pscale=pixelscale(pixsize,focal)

################### Données position ######################################

px=583 # pixels du point gps
py=1022
agvert=0.52 # tout en radian
aghoriz=0.3
bouss= 3

[el,az] = positionAZEL(px,py,agvert,aghoriz,bouss,pscale)

# print(el)
# print("\n")
# print(az)

elstring=str(abs(int(el))).ljust(7, ' ')
azstring=str(int(az)).ljust(7, ' ')

# print(elstring)
# print(azstring)

################### Conversion IOD ########################################
# données arbitraires cf http://www.satobs.org/position/IODformat.html pour les correspondances

fname="testIOD.txt"

sg=""
if el>0:
   sg="+"
else: sg="-"

angleforme="4"
time="20210329213200000"
tuncert="18"
puncert="18"
objnb="12345 98 123A  "
stnb="2007"
ststatut= "F"

conv_altaz_to_IOD(elstring,azstring,sg,angleforme,puncert,time,tuncert,objnb,stnb,ststatut,fname)

'''
