import os
from PIL import Image
from  calculate_zhibiao import  calculate_image_metric


def check_path_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False

def is_image(file_path):
    try:
        img = Image.open(file_path)
        img.verify()  # 尝试验证文件
        img.close()
        return True
    except (IOError, SyntaxError):
        return False



def getmeritslList(ctpath, generatepath ,merits):
    y_all={}
    for merit in merits:
            y = []
            for ctfilename, generatefilename in zip(os.listdir(ctpath), os.listdir(generatepath)):
                path1 = os.path.join(ctpath, ctfilename)
                path2 = os.path.join(generatepath, generatefilename)
                y.append(calculate_image_metric(path1, path2, merit, False))
            y_all[merit]=y
    return y_all