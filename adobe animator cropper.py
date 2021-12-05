from bs4 import BeautifulSoup
from pathlib import Path
import os
from PIL import Image as Image, ImageOps
import ntpath
from easygui import *

# 1 select a inputfile
inputFileName = fileopenbox('Please choose a XML or PNG file','', '*.*')

path, ext = os.path.splitext(inputFileName)
base = os.path.dirname(inputFileName)

deffile = os.path.join(path + ".xml")
imgfile = os.path.join(path + ".png")


def parseFileAndMakeImage(deffile, imgfile):

    infile = open(deffile,"r", encoding='utf-8')
    contents = infile.read()

    soup = BeautifulSoup(contents, 'lxml-xml')

    line = soup.findAll('SubTexture')

    Path(os.path.join(base, path + "_crop")).mkdir(parents=True, exist_ok=True)

    maxWidth = 0
    maxHeight = 0
    for idx in range(len(line)): 
        aLine = line[idx]
        name = aLine["name"]
        h = int(aLine["height"])
        w = int(aLine["width"])
        try:
            fw = int(aLine["frameWidth"])
            fh = int(aLine["frameHeight"])
        except:
            fw = w
            fh = h

        if maxWidth < fw :
            maxWidth = fw

        if maxHeight < fh :
            maxHeight = fh

    print("가장 큰 width {}".format(maxWidth))
    print("가장 큰 height {}".format(maxHeight))


    for idx in range(len(line)): 
        # break # 임시로 끄기

        aLine = line[idx]
        name = aLine["name"]
        
        h = int(aLine["height"])
        w = int(aLine["width"])
        x = int(aLine["x"])
        y = int(aLine["y"])
        try:
            fw = int(aLine["frameWidth"])
            fh = int(aLine["frameHeight"])
            fx = int(aLine["frameX"])
            fy = int(aLine["frameY"])
        except:
            fw = w
            fh = h
            fx = 0
            fy = 0
        # print("name : ", name, " width : ", width)

        # if idx < 58:
        #     continue

        #if 'stand' not in name:
        #    continue

        # 같은 이미지가 많은 이유는 animator 의 멈춰있는 시간까지 계산에 넣었기 때문이다.
        # if idx >= 1 :
        #     if defs[idx - 1]['height'] == defs[idx - 0]['height'] and defs[idx - 1]['width'] == defs[idx - 0]['width'] \
        #             and defs[idx - 1]['y'] == defs[idx - 0]['y'] and defs[idx - 1]['x'] == defs[idx - 0]['x']:
        #         print('같은 이미지 버리기 name : ', name)
        #         continue

        org = Image.open(imgfile)

        cropped = org.crop((x, y, x + w, y + h))

        canvas_img_path = os.path.join(base, path + "_crop", 'canvas ' + name + '.png')

        ox = 0
        oy = 0

        if "shaggy_up" in name:
            ox = -6

        if "shaggy_right" in name:
            ox = -20
            oy = -40
        if "shaggy_left" in name:
            ox = 100
            oy = -120
        if "shaggy_down" in name:
            oy = -170

        dx_left = 100
        dx_right = -20
        dy = 0
        
        # new_canvas = (fw, fh)
        new_canvas = (maxWidth + dx_left + -dx_right, maxHeight)
        new_image = Image.new("RGBA", new_canvas)
        
        print("name : ", name, " width : ", w, " height[", h, "], x[", x, "], y[",
            y, "], fx[", fx, "], fy[", fy, "], fw[", fw, "], fh[", fh, "]")

        # if fx > 0:
        #     fx = 0
        # if fy > 0:
        #     fy = 0

        # animation.addByPrefix('idle', 'shaggy_idle', 24);
        # animation.addByPrefix('idle2', 'shaggy_idle2', 24);
        # animation.addByPrefix('singUP', 'shaggy_up', 30);
        # animation.addByPrefix('singRIGHT', 'shaggy_right', 30);
        # animation.addByPrefix('singDOWN', 'shaggy_down', 30);
        # animation.addByPrefix('singLEFT', 'shaggy_left', 30);

        # addOffset('idle');
        # addOffset('idle2');
        # addOffset("singUP", -6, 0)
        # addOffset("singRIGHT", -20, -40);
        # addOffset("singLEFT", 100, -120);
        # addOffset("singDOWN", 0, -170); 


        

        pasteX = -fx -ox + dx_left
        pasteY = -fy -oy 

        print("pasteX : " + str(pasteX) + ", pasteY : " + str(pasteY))

        new_image.paste(cropped, (pasteX, pasteY))
        new_image.save(canvas_img_path)
        # cropped.save(tight_img_path)


        # org.save(filename = os.path.join(base, 'crop', 'b' + name + '.png'))

parseFileAndMakeImage(deffile, imgfile)