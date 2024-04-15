from calculate_psnr import compute_quality
import cv2
import numpy as np
import math
import os
import glob
import shutil

def find_all_data(folder_path, file_extension):
    yms_file = []
    root = []
    for r, d, f in os.walk(folder_path):  # r= root; d = directory; f = file
        for file in f:
            if (file_extension in file):
                # files.append(os.path.join(r, file))
                # print(r)
                # yms_file[r] = file
                root.append(r)
                yms_file.append(r+"/"+file)


    #root = sorted(root)
    #yms_file = sorted(yms_file)

    return yms_file


rgb_img_path = "/home/hri/Documents/gta_test_2_test/validation/rgb/imgs/GTA_validation_0/" # source folder for rgb images
thermal_translated_imgs= "/home/hri/Documents/gta_test_2_test/validation/tir_temp/GTA_validation_0/" # source folder path for translated images
num_styles = 80
rgb_scenes = sorted(os.listdir(rgb_img_path))
tir_scenes = sorted(os.listdir(thermal_translated_imgs))

#rgb_images = sorted(glob.glob(rgb_img_path+"*/*.jpg"))

#print(rgb_images)
#assert len(rgb_scenes) == len(tir_scenes)
psnr_arr = np.zeros([len(rgb_scenes),num_styles],dtype=np.float64)
ssim_arr = np.zeros([len(rgb_scenes),num_styles],dtype=np.float64)
#dir_name_arr = [[],[]]
for scene in rgb_scenes:
    rgb_images = sorted(glob.glob(rgb_img_path +scene+"/*.jpg"))
    thermal_image_dir = sorted(os.listdir(thermal_translated_imgs+scene))
    print(thermal_image_dir)
    for styles in range(len(thermal_image_dir)):
        #print(thermal_translated_imgs+str(thermal_image_dir[styles]))
        folder_path = thermal_translated_imgs+scene+"/"+str(thermal_image_dir[styles])
        tir_imgs = sorted(glob.glob(folder_path+"/*.jpg"))
        #print(tir_imgs,folder_path+"/*.jpg")
        assert(len(tir_imgs)==len(rgb_images))
        #dir_name_arr[int(scene) - 1][ styles] = folder_path
        for img_idx in range(len(tir_imgs)):
            tir = tir_imgs[img_idx]
            rgb = rgb_images[img_idx]
            assert (rgb_images[img_idx][-13:] == tir_imgs[img_idx][-13:])

            ssim_score, psnr_score = compute_quality(rgb,tir)
            psnr_score=np.float64(psnr_score)
            #print(type(ssim_score),type(psnr_score))
            #print(ssim_arr[int(scene)][styles],psnr_arr[int(scene)][styles])

            psnr_arr[int(scene)-1][styles] = psnr_arr[int(scene)-1,styles] + psnr_score
            ssim_arr[int(scene)-1, styles] = ssim_arr[int(scene)-1, styles] + ssim_score

            #print(tir_imgs[img_idx][-13:])
            #print(rgb_images[img_idx][-13:])
            #assert(rgb_images[img_idx][-13:] == tir_imgs
            # [img_idx][-13:])




print(np.argmax(psnr_arr,1))
max_ssim = np.argmax(ssim_arr,1)
max_psnr = np.argmax(psnr_arr,1)
print("clearning folders")
print(max_ssim)
print(max_psnr)
#for best in range(len(max_ssim)):

 #   if (max_ssim[best] == max_psnr[best]):
        # delete the rest
  #      src = thermal_translated_imgs+rgb_scenes[best]+"/"+sorted(os.listdir(thermal_translated_imgs+"/"+rgb_scenes[best]))[max_ssim[best]]
   #     dst = save_dir+rgb_scenes[best]+"/"
    #    if os.path.exists(dst):
     #       shutil.rmtree(dst)
      #  shutil.copytree(src,dst,copy_function=shutil.copy2)
