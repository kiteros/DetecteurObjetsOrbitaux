from PIL import Image, ImageEnhance, ImageFilter
from PIL.ImageFilter import  GaussianBlur

def filtre(img,contrast_factor=0.2,brightness_factor=9):

    enhancer = ImageEnhance.Contrast(img)
    filtred_img = enhancer.enhance(contrast_factor)

    enhancer2 = ImageEnhance.Brightness(filtred_img)
    filtred_img = enhancer2.enhance(brightness_factor)

    #filtred_img = filtred_img.filter(GaussianBlur(radius=2))

    thresh = 100
    fn = lambda x: 255 if x > thresh else 0
    filtred_img = filtred_img.convert('L').point(fn, mode='1')
    filtred_img =filtred_img.convert("RGB")


    return filtred_img