# 
import cv2
import os
import numpy as np
import copy


def mask_overlap(image, mask_, color_bgr):
    mask_ = np.dstack((mask_, mask_, mask_))

    index = mask_[:, :, 1] == 0

    mask_ = np.int64(mask_ < 1)
    mask_ = mask_*np.array(color_bgr)

    mask_ = mask_.astype(np.uint8)
    weight_coeffi = cv2.addWeighted(mask_, 0.8, image, 0.2, 0.)
    # cv2.imwrite('weight.png', weight_coeffi)

    image_ = copy.copy(image)

    image_[index] = weight_coeffi[index]

    return image_


def main():
    filelist = os.listdir(path_image)
    for files in filelist:  # files=name+jpg
            filename = os.path.splitext(files)[0]
            filepath = path_image + files

            name = filename.split("%")[0]
            src_name = name + '.png'
            src_path = path_src + src_name

            try:
                mask = cv2.imread(filepath, -1)
                src = cv2.imread(src_path, )
            except Exception:
                print ('The filepath (image) is not found!')
                raise
            image_size = mask.shape[0]
            src = cv2.resize(src, (image_size, image_size))
            img_mask = mask_overlap(src, mask, color_bgr=[0, 128, 192])

            cv2.imwrite(path_ + src_name, img_mask)


if __name__ == "__main__":
    path_image = "./out_image/"
    path_src = "./src/"
    path_ = "./src_with_mask/"
    main()
