from rasp_full_process import *
import os

def read_img_name(param):
    token = open(param, 'r')
    linestoken = token.readlines()
    tokens_column_number = 0
    resulttoken = []
    for x in linestoken:
        resulttoken.append(x.split()[tokens_column_number])
    token.close()
    return resulttoken

def read_img_times(param):
    token = open(param, 'r')
    linestoken = token.readlines()
    tokens_column_number = 1
    resulttoken = []
    for x in linestoken:
        resulttoken.append(x.split()[tokens_column_number])
    token.close()
    return resulttoken


def analyse_pic_from_folder(args):

    #os.chdir(args.folder)

    img_names = read_img_name('param_img.txt')
    img_times = read_img_times('param_img.txt')

    for name in img_names:
        print('Traitement de l\'image ' + name)
        outputname=name[:-4]+'_output.jpg'
        try:
            process_one_img(args,name,outputname)
        except:
            print('Erreur dans le traitement de l\'image ' + name)
            pass
