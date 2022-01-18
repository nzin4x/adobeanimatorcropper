# 3개의 파일을 동시에 넣었을 때 python 이 어떻게 받아들이는지 테스트
from pathlib import Path
import os
from PIL import Image as Image, ImageOps
from easygui import *

# 선택된 파일들의 배열
files = fileopenbox('이동할 이미지들을 선택하세요','', '*.png', multiple=True)

xy = (input("x ? y : "))
pixel = int(input("얼마나 이동 ? : "))

for idx in range(len(files)): 
    # 파일의 위치
    file_full_path = files[idx]

    # 편집 이미지 열고
    edit_image = Image.open(file_full_path)

    # 편집 이미지의 사이즈
    edit_width, edit_height = edit_image.size

    # 파일 경로
    file_path, ext = os.path.splitext(file_full_path) # extension 확장자 .xxx .png .xml split 짜르다 나누다.
    file_dir = os.path.dirname(file_full_path)
    file_name = os.path.basename(file_full_path)

    # 만들어질 이미지 경로
    save_folder = os.path.join(file_dir + "/" + (xy) + "_" + str(pixel))
    os.makedirs(save_folder, exist_ok=True)
    
    # 빈종이 만들기
    new_image = Image.new("RGBA", (edit_width, edit_height))
    if xy == 'x':
        new_image.paste(edit_image, (int((edit_width / 2) - (edit_width / 2)) + pixel, int((edit_height / 2) - (edit_height / 2))))
    if xy == 'y':
        new_image.paste(edit_image, (int((edit_width / 2) - (edit_width / 2)), int((edit_height / 2) - (edit_height / 2)) - pixel))

    new_image.save(save_folder + "/" + file_name + "." + ext)
