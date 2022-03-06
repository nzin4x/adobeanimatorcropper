# 3개의 파일을 동시에 넣었을 때 python 이 어떻게 받아들이는지 테스트
from bs4 import BeautifulSoup
from pathlib import Path
import os
import re
import sys
from PIL import Image as Image, ImageOps
from easygui import *
import argparse
import ntpath

def convert(s):
  
    # initialization of string to ""
    str1 = ""
  
    # using join function join the list s by 
    # separating words by str1
    return(str1.join(s))

# 선택된 파일들의 배열
inputFileName = fileopenbox('같은 사이즈로 만들 이미지들을 선택하세요','', '*.png', multiple=True)
width = input("가로 사이즈?")
height = input("세로 사이즈?")


print("가로 {0} 세로 {1}".format(width, height))

for idx in range(len(inputFileName)): 
    print(inputFileName[idx])


