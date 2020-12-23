import cv2
import time
import os
import sys

MAX_ANGLE = 45
ROTATE_ANGLE = 15


def image_rotate(target_img, max_ang, rotate_ang):
    """画像を回転し保存

    target_img : String
        回転対象の画像のパス

    max_ang : int
        最大回転角

    rotate_ang : float
        回転角度
    """
    # 画像を指定
    img = cv2.imread(target_img)
    # 高さを定義
    height = img.shape[0]
    # 幅を定義
    width = img.shape[1]
    # 回転の中心を指定
    center = (int(width/2), int(height/2))
    # スケールを指定
    scale = 1.0
    # ファイル名抽出
    image_file = os.path.splitext(target_img)

    for ang in range(0, max_ang+1, rotate_ang):
        # getRotationMatrix2D関数を使用
        trans = cv2.getRotationMatrix2D(center, ang, scale)
        # アフィン変換
        image2 = cv2.warpAffine(img, trans, (width, height), dst=None, flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        print(image_file[0]+"_"+str(ang)+image_file[1]+" Saved")
        cv2.imwrite(image_file[0]+"_"+str(ang)+image_file[1], image2)


def main():
    if len(sys.argv) == 2:
        target_img = sys.argv[1]
        image_rotate(target_img, MAX_ANGLE, ROTATE_ANGLE)
    else:
        print('Argument Error')


if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
