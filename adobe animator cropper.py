from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image as Image, ImageOps
import argparse
import ntpath

parser = argparse.ArgumentParser(description = "adobe animator 로 만들어진 이미지와 xml 을 이용해서 작은 이미지를 생성한다")
parser.add_argument('file', help="이미지 파일으 경로, xml 과 이름이 같아야 함")
args = parser.parse_args()

path, ext = os.path.splitext(args.file)
base = os.path.dirname(args.file)
filename = ntpath.basename(args.file)

deffile = os.path.join(path + ".xml")
imgfile = os.path.join(path + ".png")

infile = open(deffile,"r", encoding='utf-8')
contents = infile.read()

soup = BeautifulSoup(contents, 'lxml-xml')

defs = soup.findAll('SubTexture')

Path(os.path.join(base, filename + "_crop")).mkdir(parents=True, exist_ok=True)
for idx in range(len(defs)): 
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

    if 'NOTE DOWN' not in name:
        continue

    if idx >= 1 :
        if defs[idx - 1]['height'] == defs[idx - 0]['height'] and defs[idx - 1]['width'] == defs[idx - 0]['width'] \
                and defs[idx - 1]['y'] == defs[idx - 0]['y'] and defs[idx - 1]['x'] == defs[idx - 0]['x']:
            print('같은 이미지 버리기 name : ', name)
            continue

    org = Image.open(imgfile)

    cropped = org.crop((x, y, x + w, y + h))

    canvas_img_path = os.path.join(base, filename + "_crop", 'canvas ' + name + '.png')
    tight_img_path = os.path.join(base, filename + "_crop", 'tight ' + name + '.png')
    
    new_canvas = (fw, fh)
    new_image = Image.new("RGBA", new_canvas)
    
    print("name : ", name, " width : ", w, " height[", h, "], x[", x, "], y[",
          y, "], fx[", fx, "], fy[", fy, "], fw[", fw, "], fh[", fh, "]")

    # if fx > 0:
    #     fx = 0
    # if fy > 0:
    #     fy = 0

    new_image.paste(cropped, (fw - w + fx, fh - h + fy))
    new_image.save(canvas_img_path)
    # cropped.save(tight_img_path)

    # org.border(Color('transparent'), int((460 - w) / 2), int((460 - h) / 2) )
    # org.save(filename = os.path.join(base, 'crop', 'b' + name + '.png'))
