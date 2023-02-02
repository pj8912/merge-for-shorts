from moviepy.editor import *
from moviepy.video.fx.all import *


#main clip at the top
clip1 = VideoFileClip("/home/jp/Videos/time_machine.mp4") 

clip1 = clip1.crop(x1=640, y1 = 0, x2=1280, y2 = 360)
c1size = clip1.size
print('clip1: ', c1size)
# print(c1size[0], c1size[1])


# clip2 =   VideoFileClip("/home/jp/Videos/quake_short.mp4")
# # clip2 = clip2.subclip(0,5)
# print('clip2 or. size', clip2.size)
# clip2.resize(c1size[0], c1size[1])
# print('clip after resize', clip2.size)

