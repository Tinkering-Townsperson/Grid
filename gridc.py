from os.path import exists
from PIL import Image, ImageDraw
from datetime import datetime as dt
import sys, re

print("Starting...")
imgpath=gridpath = None#path to file, from sys.argv[1]
log=grid = None#file
fn=ft=ct=w=h = None#grid attributes, such as name, filetype, colortype, width, and height, respectively
iso = re.compile(r'[a-zA-Z0-9]+')#regexp for isolating letters and numbers
c = 0#temporary var for the current regexp
gdata = 0#data inside file
if len(sys.argv) == 2:
    gridpath = sys.argv[1]
    c = re.compile(r'(\w:[a-zA-Z0-9\\]+\\)[\w\d]*\.[\w\d]+')
    imgpath = c.findall(gridpath)[0]
else:
    print("Looks like you forgot to pass a filepath!")
if exists(gridpath):
    grid = open(gridpath)
    log = open("C:\\Grid\\Grid.log", mode='at')
    log.write("Start time:"+str(dt.now().strftime("%b-%d-%Y %H:%M:%S\n")))
    log.write("File:"+str(gridpath) + "\nFile descriptor:" + str(grid) + "\nFile data:")
    #print(grid)
    gdata =grid.read()
    log.write(gdata + "\nFilename:")
    #print(gdata + "\n")
    c = re.findall(r': .+\s', gdata)
    fn = iso.findall(c[0])[0]
    ft = iso.findall(c[1])[0]
    ct = iso.findall(c[2])[0]
    log.write(fn + "." + ft + "\ncolortype:" + ct + "\nGrid data(pixel art):")
    #print(fn+"."+ft,"\ncolortype:",ct)
    c = re.findall(r':START\n([\d\w\s]+)\n:END', gdata)[0]
    log.write(c.split("\n") + "\n(X, Y, Width, Height):")
    #print(c.split("\n"),"\n")
    w = len(c.split("\n")[0])
    h = len(c.split("\n"))
    log.write(c + str((w,h)) + "\n")
    #print(c, (w,h))
    if ct == "grayscale":
        im = Image.new(mode="RGB", size=(w*100,h*100))
        draw = ImageDraw.Draw(im)
        for y in range(h):
            for x in range(w):
                if c.split("\n")[y][x] == "1":
                    draw.rectangle((x*100, y*100, x*100+100, y*100+100), fill=(0, 0, 0))
                    log.write(str((x, y, w, h)))
                    #print(x, y, w, h)
                else:
                    draw.rectangle((x*100, y*100, x*100+100, y*100+100), fill=(255, 255, 255))
        im.save(imgpath+fn+'.'+ft, quality=95)
    elif ct == "color":
        print("Work in progress!")
    grid.close()
else:
    print("File doesn\'t exist!")
log.write("End time:"+dt.now().strftime("%b-%d-%Y %H:%M:%S\n"))
log.close()
