from moviepy.editor import *
from moviepy.video.fx.all import *


#main clip at the top
clip1 = VideoFileClip("/home/jp/Videos/time_machine.mp4") 
#resize clip1 if greater than 60 seconds
if clip1.duration > 60:
    clip1 = clip1.subclip(0,60) 


clip2 =   VideoFileClip("/home/jp/Videos/quake_short.mp4",audio=False)
if clip2.duration > clip1.duration:
    clip2 = clip2.subclip(0, clip1.duration)


tr1 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","top"))
tr2 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","bottom"))

clip1 = clip1.crop(x1=506, y1 = 0, x2=0, y2 = 900)
# clip2 = clip2.crop(x1=0, y1=0, x2=100, y2=0)



# [tr2]
combine = clips_array([[tr1],[clip1],[clip2],[tr2]])

import datetime
ts = datetime.datetime.now().timestamp()
filename = str(ts)+".mp4"
combine.write_videofile(filename)
# combine.preview()
combine.close()

