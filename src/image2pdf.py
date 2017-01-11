#! /usr/bin/env python
#coding=utf-8
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape
import Image,os

def convert_to_pdf1(filenamelist):
    newname=os.getcwd()+'/image/image2pdf.pdf'
    a4_w, a4_h = landscape(A4)
    c = canvas.Canvas(newname, pagesize=(a4_w, a4_h))

    for filename in filenamelist:
        im=Image.open(filename)
        im_w,im_h=im.size

        if a4_w/im_w<a4_h/im_h:
            ratio=a4_w/im_w
        else:
            ratio=a4_h/im_h

        c.drawImage(filename, 0, 0, im_w * ratio, im_h * ratio)
        c.showPage()
    c.save()

    print "convert finish"

if __name__ == "__main__":
    rootdir = os.getcwd() + '/image/'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    image_path = []
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
            image_path.append(path)

    convert_to_pdf1(image_path)