from mosaic import *
from filtre import *
from matplotlib import pyplot as plt

def main():
    inputname='pic_2021-04-16+16-37-00+m+328.jpg'
    raw_img = get_raw_image(inputname)
    #filtred_img=filtre(raw_img)
    #raw_img.save('modified_img.png')
    '''
    f, axes = plt.subplots(1, 1)
    axes.imshow(raw_img)
    plt.savefig('modified_img.png')
    '''

if __name__ == '__main__':
    main()