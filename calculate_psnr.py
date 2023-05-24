import cv2
import numpy as np
import math
from skimage.metrics import structural_similarity as ssim
from skimage import io
def compute_LoG(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    mask1 = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    mask2 = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    mask3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])

    gaussian = cv2.GaussianBlur(gray, (5, 5), 0)
    LoG = cv2.filter2D(gaussian, -1, mask3)

    return LoG

def psnr(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


def compute_quality(rgb,tir):
    """
    :param rgb: RGB image input file path
    :param tir: TIR image input file path
    :return: SSIM score, PSNR
    """
    rgb_LoG = compute_LoG(rgb)
    tir_LoG = compute_LoG(tir)

    # print(rgb_LoG.shape, tir_LoG.shape)

    psnr_score = psnr(rgb_LoG, tir_LoG)
    (score, diff) = ssim(rgb_LoG, tir_LoG, full=True)
    diff = (diff * 255).astype("uint8")

    #print("SSIM: {}".format(score))
    #print("PSNR: {}".format(psnr_score))

    return score, psnr_score

#tir="/home/hri/PycharmProjects/Thermal_optical_flow/MUNIT/inference_test/27_out_35/027_00450valid.jpg"
#rgb="/home/hri/PycharmProjects/Thermal_optical_flow/MUNIT/inference_test/27_test/027_00450valid.jpg"

#score, psnr = compute_quality(rgb,tir)