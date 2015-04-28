#!/usr/bin/env/python
#coding: utf-8
from __future__ import unicode_literals
import os
import gc
import random
from PIL import Image
from PIL import ImageEnhance
from time import sleep


class WallpaperControl(object):
    folder = '/home/carlos/wallpapers/'
    cache = os.path.join(folder, '.cache')
    time = 15
    darken = 0.2
    files = []

    def __init__(self):
        if not os.path.isdir(self.cache):
            os.mkdir(self.cache)

    def loop(self):
        self.update_files()
        for f in self.get_files():
            self.set_wallpaper(f)
            sleep(self.time)

    def update_files(self):
        files = []
        for f in os.listdir(self.folder):
            filename = os.path.join(self.folder, f)
            if os.path.isfile(filename) and self.is_image(filename):
                files.append(filename)

        random.shuffle(files)
        self.files = files

    def is_image(self, s):
        s = s.lower()
        return '.jpg' in s or '.png' in s or '.jpeg' in s

    def get_cached_name(self, filename):
        cached = os.path.join(self.cache, os.path.basename(filename))
        names = cached.split('.')
        ext = names.pop()
        name = '.'.join(names)
        return '{}.{}.{}'.format(name, self.darken, ext)

    def get_edited(self, filename):
        cached = self.get_cached_name(filename)

        if not os.path.exists(cached):
            im = Image.open(filename)
            im = ImageEnhance.Contrast(im)
            im = im.enhance(0.8)
            im = ImageEnhance.Color(im)
            im = im.enhance(0.5)
            im = ImageEnhance.Brightness(im)
            im = im.enhance(self.darken)
            overlay = Image.new(im.mode, im.size, '#005e5f')
            im = Image.blend(im, overlay, 0.45)
            im = ImageEnhance.Brightness(im)
            im = im.enhance(0.7)
            im.save(cached)

            del im
            gc.collect()

        return cached

    def get_files(self):
        for filename in self.files:
            yield self.get_edited(filename)

    def set_wallpaper(self, wallpaper):
        wallpaper = '"{}"'.format(wallpaper)
        os.system('feh --bg-fill {}'.format(wallpaper))

try:
    while True:
        WallpaperControl().loop()
except KeyboardInterrupt:
    print 'Stoped!'
