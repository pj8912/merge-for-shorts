from moviepy.editor import *
from moviepy.video.fx.all import *


#main clip at the top
clip1 = VideoFileClip("/home/jp/Videos/time_machine.mp4") 
#resize clip1 if greater than 60 seconds
if clip1.duration > 60:
    clip1 = clip1.subclip(0,60) #shorts max length is 60 seconds

#check clip1 duration[60< or 60 >]
# print('clip1 duration: ',  str(clip1.duration), 'seconds')



#clip at the bottom,[minecraft, fifa, small mobile games,GTA,Temple Run, Life Hacks]
#set audio false

clip2 =   VideoFileClip("/home/jp/Videos/quake_short.mp4",audio=False)
if clip2.duration > clip1.duration:
    clip2 = clip2.subclip(0, clip1.duration)
    

    
    
#clip1, clip2 ready
#get transpet images and set their durations and positions

tr1 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","top"))
tr2 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","bottom"))


w,h = clip1.size

clip1 = clip1.crop(x1=640, y1 = 0, x2=1280, y2 = 360)
# clip12 = clip1.crop(x1=640, y1 = 0, x2=1280, y2 = 360)
# clip2 = clip2.crop(x1=640, y1 = 0, x2=1280, y2 = 360)


#combine
combine = clips_array([[tr1],[clip1],[clip2],[tr2]])
# combine = clip_arrays([[tr2], [clip1],[tr2]])
# combine = clips_array([[clip1],[clip2]])
import datetime
ts = datetime.datetime.now().timestamp()
filename = str(ts)+".mp4"
combine.write_videofile(filename)
combine.close()

