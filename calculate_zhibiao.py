import os

import numpy as np
from skimage import io, color, metrics
import cv2
from skimage.metrics import structural_similarity as sk_cpt_ssim
from skimage.metrics import structural_similarity as sk_cpt_pnsr


def calculate_ssim(cbct_path, ct_path):
    # 读取CBCT图像和CT图像
    cbct_img = cv2.imread(cbct_path, cv2.IMREAD_GRAYSCALE)
    ct_img = cv2.imread(ct_path, cv2.IMREAD_GRAYSCALE)

    # 计算SSIM相似度
    ssim = sk_cpt_ssim(cbct_img, ct_img)
    print(cbct_path+"   "+ct_path+":"+str(ssim))
    return ssim
def calculate_image_metric(image_path1, image_path2, metric_type='ssim',IsPrint=True):
    try:
        # 读取两张图像
        image1_gray = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
        image2_gray = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)



        if metric_type == 'ssim':
            # 计算SSIM
            metric_value = metrics.structural_similarity(image1_gray, image2_gray)
            if IsPrint:
                print(f'SSIM值为: {metric_value}')
        elif metric_type == 'mse':
            # 计算MSE（均方误差）
            diff = image1_gray - image2_gray
            mse = (diff ** 2).mean()
            metric_value = mse
            if IsPrint:
                print(f'MSE值为: {metric_value}')
        elif metric_type == 'psnr':
            # 计算PSNR（峰值信噪比）
            mse = ((image1_gray - image2_gray) ** 2).mean()
            psnr = 10 * (np.log10((255 ** 2) / mse))
            metric_value = psnr
            if IsPrint:
                print(f'PSNR值为: {metric_value}')
        else:
            return "无效的指标类型"

        return metric_value
    except Exception as e:
        return str(e)

# # 使用示例
# desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
# image_path1 = os.path.join(desktop_path,"result","4-27.bmp")
# image_path2 =os.path.join(desktop_path,"result","4_real.png")
#
# ssim_value = calculate_image_metric(image_path1, image_path2, metric_type='ssim')
# print(f'SSIM值为: {ssim_value}')
#
# mse_value = calculate_image_metric(image_path1, image_path2, metric_type='mse')
# print(f'MSE值为: {mse_value}')
#
# psnr_value = calculate_image_metric(image_path1, image_path2, metric_type='psnr')
# print(f'PSNR值为: {psnr_value}')
