from detect_position import time_from_str_to_datetime

def read_param(param_filename):

    parametres = open(param_filename, "r")

    entete = parametres.readline().rstrip('\n\r').split(",")
    param = parametres.readline().rstrip('\n\r').split(",")

    boussoleidx = entete.index("Boussole")
    anglevertidx = entete.index("AngleVert")
    anglehorizidx = entete.index("AngleHoriz")
    focalidx = entete.index("Focale")
    pixelsizeidx = entete.index("Pixsize")
    stationnbidx = entete.index("StationNumber")
    stationstatutidx = entete.index("StationStatut")
    timeexposidx= entete.index("TmpsExposition") #en secondes
    timeidx=entete.index("Time")
    #nameinputidx=entete.index("Input")
    #nameoutputidx=entete.index("Output")

    focal=float(param[focalidx])
    pixsize=float(param[pixelsizeidx])
    agvert=float(param[anglevertidx])
    aghoriz=float(param[anglehorizidx])
    bouss=float(param[boussoleidx])
    stnb=param[stationnbidx]
    ststatut = param[stationstatutidx]
    texpos=float(param[timeexposidx])
    timestr=param[timeidx]

    time=time_from_str_to_datetime(timestr)
    #inputname=param[nameinputidx]
    #outputname=param[nameoutputidx]

    return time,agvert,aghoriz,bouss,stnb,ststatut,texpos,focal,pixsize