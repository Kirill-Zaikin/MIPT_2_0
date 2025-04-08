import cv2
import math as m
import numpy as np
from ultralytics import YOLO

# Пути до видео
VIDEO_LEFT = "D:\Desktop\MIPT\Project_Comp_SEE/09_41_36_up/left.mp4"
VIDEO_RIGHT = "D:\Desktop\MIPT\Project_Comp_SEE/09_41_36_up/right.mp4"
left_video = cv2.VideoCapture(VIDEO_LEFT)
right_video = cv2.VideoCapture(VIDEO_RIGHT)

# Матрицы гомографии
HOMO_LEFT = np.load("D:\Desktop\MIPT\Project_Comp_SEE/left_down.npy")
HOMO_LEFT_INV = np.linalg.inv(HOMO_LEFT) # инвариантная матрица
HOMO_RIGHT = np.load("D:\Desktop\MIPT\Project_Comp_SEE/right_down.npy")
HOMO_RIGHT_INV = np.linalg.inv(HOMO_RIGHT) # инвариантная матрица
Y_OFFSET_CM = 60

# веса и детектор
PALETE_WEIGHTS = "D:\Desktop\MIPT\Project_Comp_SEE/pallet_n_352_seg.pt"
segmenter = YOLO(PALETE_WEIGHTS)


def apply_homography(homography_matrix, dot_pix, need_int: bool = False): 
    '''Применяет гомографическое преобразование для точки dot_pix с помощью матрицы homography_matrix'''
    if len(dot_pix) == 2:
        dot_pix = (dot_pix[0], dot_pix[1], 1)
    res = np.dot(homography_matrix, dot_pix)
    if need_int:
        return int(res[0] / res[2]), int(res[1] / res[2])
    return res[0] / res[2], res[1] / res[2]


def preparation_poly(img, mask, cam_num, visualize):
    '''Накладывает маску на изображение, прощитывает крайние точки на полигоне, возвращает координату в пикселях'''
    if visualize:
        img[mask != 0] = (255, 255, 255)
    y, x = np.nonzero(mask)
    k1, k2 = np.polyfit(x, y, 1) # аппроксимация 1 порядка
    max_x, min_x = np.max(x), np.min(x)
    if cam_num == 0:
        return max_x, int(max_x * k1 + k2)
    else:
        return min_x, int(min_x * k1 + k2)


def get_biggest_mask(dets):
    '''фильтрует поступившие маски по размеру и берет самую большую'''
    if type(dets) is type(None):
        return None
    if dets.shape[0] == 1:
        contours, hierarchy = cv2.findContours(dets[0].astype("uint8"), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        contour = max(contours, key=cv2.contourArea)
        return cv2.drawContours(np.zeros_like(dets[0]), [contour], -1, 1, cv2.FILLED)
    else:
        contours, hierarchy = cv2.findContours(max(dets, key=np.sum).astype("uint8"), cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)
        contour = max(contours, key=cv2.contourArea)
        return cv2.drawContours(np.zeros_like(dets[0]), [contour], -1, 1, cv2.FILLED)


def get_dets(model, img1, img2):
    '''достает маски из нейронки и отправляет в CPU'''
    dets = model.predict([img1, img2])
    dets = [det.masks.data.cpu().numpy() if det.masks is not None else None for det in dets]
    return (get_biggest_mask(dets[0]), get_biggest_mask(dets[1]))


def draw_pallet_side_points_and_center_points(left_im, right_im, left_dot_cm, right_dot_cm, left_dot_pix,
                                              right_dot_pix, zero_zero_pt_left, zero_zero_pt_right, font=cv2.FONT_HERSHEY_SIMPLEX):
    '''Отрисовка начал координат погрузчика и паллеты и значений'''
    cv2.putText(right_im, f"{right_dot_cm[0]:.1f} {right_dot_cm[1]:.1f}",
                (right_dot_pix[0] + 4,right_dot_pix[1] + 4),
                font, 0.5, (255, 0, 255), 1)
    cv2.putText(left_im, f"{left_dot_cm[0]:.1f} {left_dot_cm[1]:.1f}",
                (left_dot_pix[0] + 4, left_dot_pix[1] + 4),
                font, 0.5, (255, 0, 255), 1)
    cv2.circle(right_im, (int(zero_zero_pt_right[0]), int(zero_zero_pt_right[1])), 2, (0, 255, 255), 2)
    cv2.circle(left_im, (int(zero_zero_pt_left[0]), int(zero_zero_pt_left[1])), 2, (0, 255, 255), 2)

def draw_middle_pallet_point(left_im, right_im, homog_left_inv, homog_right_inv, center_dot_cm):
    '''Отрисовка центра паллеты'''
    center_pallet_pix_left = apply_homography(homog_left_inv, center_dot_cm)
    center_pallet_pix_right = apply_homography(homog_right_inv, center_dot_cm)
    cv2.circle(right_im, (int(center_pallet_pix_right[0]), int(center_pallet_pix_right[1])), 2, (255, 255, 0), 2)
    cv2.circle(left_im, (int(center_pallet_pix_left[0]), int(center_pallet_pix_left[1])), 2, (255, 255, 0), 2)


def main(video_left, video_right, model, homo_left, homo_right, homo_left_inv, homo_right_inv):
    
    visualize = True
    pt_between_forks_left = apply_homography(homo_left_inv, (0, 0))
    pt_between_forks_right = apply_homography(homo_right_inv, (0, 0))
    while True:
        ret_left, im_left  = video_left.read()
        ret_right, im_right = video_right.read()
        dets = get_dets(model, im_right, im_left)
        if dets[0] is None or dets[1] is None:
            print('\033[93mpallet not found\033[0m')
            median_angle, dist, horiz_angle = None, None, None
        else:
            pallet_pt_r = preparation_poly(im_right, dets[0], 0, visualize)
            pallet_pt_l = preparation_poly(im_left, dets[1], 1, visualize)

            x_cm_right, y_cm_right = apply_homography(homo_left, pallet_pt_r)
            x_cm_left, y_cm_left = apply_homography(homo_right, pallet_pt_l)
            draw_pallet_side_points_and_center_points(im_left, im_right, (x_cm_left, y_cm_left),
                                                      (x_cm_right, y_cm_right), pallet_pt_l, pallet_pt_r,
                                                      pt_between_forks_left, pt_between_forks_right)
            pallet_len = ((x_cm_right - x_cm_left) ** 2 + (y_cm_left - y_cm_right) ** 2) ** 0.5


            x_cm_center, y_cm_center = (x_cm_right + x_cm_left) / 2, (y_cm_right + y_cm_left) / 2
            median_angle = -m.atan2(x_cm_center, y_cm_center + Y_OFFSET_CM)
            dist = np.linalg.norm((x_cm_center, y_cm_center)) / 100
            horiz_angle = m.atan((y_cm_right - y_cm_left) / (x_cm_right - x_cm_left))

            draw_middle_pallet_point(im_left, im_right, homo_left_inv, homo_right_inv,
                                     (x_cm_center, y_cm_center))
        cv2.imshow('left_pallet', im_left)
        cv2.imshow('right_pallet', im_right)
        cv2.waitKey(1)

main(left_video, right_video, segmenter, HOMO_LEFT, HOMO_RIGHT, HOMO_LEFT_INV, HOMO_RIGHT_INV)