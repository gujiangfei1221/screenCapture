#!/usr/bin/python
# -*- coding: utf-8 -*-

import Image,os

def make_regalur_image(img, size = (256, 256)):
    return img.resize(size).convert('RGB')

def split_image(img, part_size = (64, 64)):
    w, h = img.size
    pw, ph = part_size
    
    assert w % pw == h % ph == 0
    
    return [img.crop((i, j, i+pw, j+ph)).copy() \
                for i in xrange(0, w, pw) \
                for j in xrange(0, h, ph)]

def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    return sum(1 - (0 if l == r else float(abs(l - r))/max(l, r)) for l, r in zip(lh, rh))/len(lh)

def calc_similar(li, ri):
    return sum(hist_similar(l.histogram(), r.histogram()) for l, r in zip(split_image(li), split_image(ri))) / 16.0
            

def calc_similar_by_path(lf, rf):
    li, ri = make_regalur_image(Image.open(lf)), make_regalur_image(Image.open(rf))
    return calc_similar(li, ri)

def handleImage():
    rootdir = os.getcwd()+'/image/'
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    image_path = []
    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        if os.path.isfile(path):
                image_path.append(path)

    for i in range(0,len(image_path)-1):
        similar = calc_similar_by_path(image_path[i],image_path[i+1])
        print(similar)
        if( similar>= 1):
            os.remove(image_path[i])

if __name__ == '__main__':
    handleImage()


