# 3개의 파일을 동시에 넣었을 때 python 이 어떻게 받아들이는지 테스트
from pathlib import Path
import os
from PIL import Image as Image, ImageOps
from easygui import *

# 선택된 파일들의 배열
files = fileopenbox('같은 사이즈로 만들 이미지들을 선택하세요','', '*.png', multiple=True)

print(files)

target_width = int(input("가로 사이즈? "))
target_height = int(input("세로 사이즈? "))

print("선택된 파일 갯수 : " + str(len(files)))

print("가로 {0} 세로 {1}".format(target_width, target_height))

for idx in range(len(files)): 
    print("파일번호" + str(idx))

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
    save_folder = os.path.join(file_dir + "/" + str(target_width) + "x" + str(target_height))
    os.makedirs(save_folder, exist_ok=True)
    
    # 빈종이 만들기
    new_image = Image.new("RGBA", (target_width, target_height))
    new_image.paste(edit_image, (int((target_width / 2) - (edit_width / 2)), int((target_height / 2) - (edit_height / 2))))
    new_image.save(save_folder + "/" + file_name)
