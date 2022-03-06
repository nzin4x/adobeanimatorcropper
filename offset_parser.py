from bs4 import BeautifulSoup
from pathlib import Path
import os
import re
from PIL import Image as Image, ImageOps
import argparse
import ntpath
from easygui import *

# 1 select a inputfile
aTXT = fileopenbox('Please choose a TXT file','', '*.txt')

offsetFile = aTXT

infile = open(offsetFile,"r", encoding='utf-8')
contents = infile.readlines()

for aLine in contents:
    tabs = aLine.split(" ")

    name = tabs[0]
    offsetX = tabs[1]
    offsetY = tabs[2]

    # print("{} offset X = {}, offset y = {}".format(name, offsetX, offsetY))

    p = re.compile('[A-Z]+')
    m = p.findall(name)

    # print("{} is, {} is uppercase".format(name, m))

    if len(m) == 0:
        name = name
    else:
        name = m[0]


    name = name.lower()

    print("name is {}".format(name))