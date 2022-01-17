from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image as Image, ImageOps
import argparse
import ntpath

# 파일을 가져와서 이미지와 xml 을 나눈다.
parser = argparse.ArgumentParser(description = "adobe animator 로 만들어진 이미지와 xml 을 이용해서 작은 이미지를 생성한다")
parser.add_argument('file', help="이미지 파일으 경로, xml 과 이름이 같아야 함")
args = parser.parse_args()

path, ext = os.path.splitext(args.file) # extension 확장자 .xxx .png .xml split 짜르다 나누다.
base = os.path.dirname(args.file)
filename = ntpath.basename(args.file)

deffile = os.path.join(path + ".xml") # definition 정의 파일
imgfile = os.path.join(path + ".png") # image file 이미지 파일




# xml 열어서 beautifulsoup 로 분석시킨다.
infile = open(deffile,"r", enco일ing='utf-8')
contents = infile.read() # 컨텐츠. 내용

soup = BeautifulSoup(contents, 'lxml-xml')

defs = soup.findAll('SubTexture')

Path(os.path.join(base, filename + "_crop")).mkdir(parents=True, exist_ok=True)





for idx in range(len(defs)): 

    # xml 내용을 모두 변수에 담는다.

    iDef = defs[idx]
    name = iDef["name"]
    
    h = int(iDef["height"])
    w = int(iDef["width"])
    x = int(iDef["x"])
    y = int(iDef["y"])
    try:
        fw = int(iDef["frameWidth"])
        fh = int(iDef["frameHeight"])
        fx = int(iDef["frameX"])
        fy = int(iDef["frameY"])
    except:
        fw = w
        fh = h
        fx = 0
        fy = 0
    # print("name : ", name, " width : ", width)

    # if idx < 58:
    #     continue

    # if 'NOTE DOWN' not in name:
    #    continue

    if idx >= 1 :
        if defs[idx - 1]['height'] == defs[idx - 0]['height'] and defs[idx - 1]['width'] == defs[idx - 0]['width'] \
                and defs[idx - 1]['y'] == defs[idx - 0]['y'] and defs[idx - 1]['x'] == defs[idx - 0]['x']:
            print('같은 이미지 버리기 name : ', name)
            continue



    # 이미지 열고
    org = Image.open(imgfile)

    # 자르고
    cropped = org.crop((x, y, x + w, y + h))

    # 만들어질 이미지 경로
    canvas_img_path = os.path.join(base, filename + "_crop", 'canvas ' + name + '.png')
    tight_img_path = os.path.join(base, filename + "_crop", 'tight ' + name + '.png')
    
    # 빈종이 만들기
    new_canvas = (fw, fh)
    new_image = Image.new("RGBA", new_canvas)
    
    print("name : ", name, " width : ", w, " height[", h, "], x[", x, "], y[",
          y, "], fx[", fx, "], fy[", fy, "], fw[", fw, "], fh[", fh, "]")

    # if fx > 0:
    #     fx = 0
    # if fy > 0:
    #     fy = 0

    # 빈종이에 이미지 붙여 넣기 / 저장하기
    new_image.paste(cropped, (fw - w + fx, fh - h + fy))
    new_image.save(canvas_img_path)
    # cropped.save(tight_img_path)

    # org.border(Color('transparent'), int((460 - w) / 2), int((460 - h) / 2) )
    # org.save(filename = os.path.join(base, 'crop', 'b' + name + '.png'))
