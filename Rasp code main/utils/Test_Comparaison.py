import utils.prologue as prologue
from utils.read_param import *

def main(args):

    inputname, outputname, agvert, aghoriz, bouss, stnb, ststatut, texpos, focal, pixsize=read_param(args.param)

    Mx1=342
    My1=594
    Mx2 = 517
    My2 = 329
    Mx3 = 655
    My3 = 128

    datereal='2021041621'

    t=time_middle(date,texpos)



if __name__ == '__main__':
    main(prologue.get_args())
