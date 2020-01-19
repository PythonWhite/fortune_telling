import random

from captcha.image import ImageCaptcha


CHARTS = 'abcdefghijklmnopqrestuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def gen_captcha(num=4):
    text=''
    for i in range(0, num):
        text +=random.choice(CHARTS)
    image = ImageCaptcha()
    data = image.generate(text)
    return text, data.read()


def check_pass(code, captcha_code):
    if not isinstance(code, str) or not isinstance(captcha_code, str):
        return False
    if code.upper() == captcha_code.upper():
        return True

    return False
    