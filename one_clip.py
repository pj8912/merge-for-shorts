from moviepy.editor import *
from moviepy.video.fx.all import *


#main clip at the top
clip1 = VideoFileClip("/home/jp/Videos/time_machine.mp4") 
#resize clip1 if greater than 60 seconds
if clip1.duration > 60:
    clip1 = clip1.subclip(0,59)


clip1 = clip1.crop(x1=640, y1 = 0, x2=1280, y2 = 360)


tr1 = ImageClip("test/fondo.png").set_duration(clip1.duration).set_position(("center","top"))
tr2 = ImageClip("test/fondo.png").set_duration(clip1.duration).set_position(("center","bottom"))

combine = clips_array([[tr1],[clip1][tr2]])

import datetime
ts = datetime.datetime.now().timestamp()

filename = str(ts)+".mp4"
combine.write_videofile(filename)
combine.close()