import random

from captcha.image import ImageCaptcha


CHARTS = 'abcdefghijklmnopqrestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def gen_captcha(num=4):
    text=''
    for i in range(0, num):
        text +=random.choice(CHARTS)
    data = ImageCaptcha().generate(text)
    return text, data
