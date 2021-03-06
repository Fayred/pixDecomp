#coding:utf-8

import argparse
from PIL import Image

def pixDecomp(picture, filename):
    im = Image.open(picture).convert('1')
    width, height = im.size
    pixelsImg = im.load()
    pixelsDecomp = []
    for y in range(height):
        pixelsDecomp.append([("0", "1")[pixelsImg[x, y] == 255] for x in range(width)])
    with open(filename, "w") as f:
        for pixel in pixelsDecomp:    
            f.write("".join(pixel)+"\n")

def pixComp(filename, picture):
    pixelsDecomp = open(filename).read().split()
    width = len(pixelsDecomp[0])
    height = len(pixelsDecomp)
    im = Image.new("1", (width, height))
    pixels = im.load()
    for y in range(height):
        for x in range(width):
            pixels[x, y] = int(pixelsDecomp[y][x])
    im.save(picture)

parser = argparse.ArgumentParser()
parser.add_argument("-d", action="store_true", help="decompose an image")
parser.add_argument("-c", action="store_true", help="recompose an image")
parser.add_argument("-i", metavar="image", help="name of image")
parser.add_argument("-f", metavar="filename", help="filename")
args = parser.parse_args()

if (args.d == True and args.f != None
and args.i != None and args.c == False):
    pixDecomp(args.i, args.f)
elif (args.c == True and args.f != None
and args.i != None and args.d == False):
    pixComp(args.f, args.i)
else:
    parser.print_help()