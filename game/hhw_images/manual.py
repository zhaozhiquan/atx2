# -*- encoding: utf-8 -*-
#
# Created on: Thu Aug 03 14:00:48 2017


import os
import atx


d = atx.connect(os.getenv("SERIAL"))
images =  d.exists('guide_46.1920x1080.png')
print images