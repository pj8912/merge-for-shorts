from moviepy.editor import *
from moviepy.video.fx.all import *


#main clip at the top
clip1 = VideoFileClip("/home/jp/Videos/stewie_praying.mp4") 
#resize clip1 if greater than 60 seconds
if clip1.duration > 60:
    clip1 = clip1.subclip(0,60) #shorts max length is 60 seconds

#check clip1 duration[60< or 60 >]
# print('clip1 duration: ',  str(clip1.duration), 'seconds')



#clip at the bottom,[minecraft, fifa, small mobile games,GTA,Temple Run, Life Hacks]
clip2 =   VideoFileClip("/home/jp/Videos/quake_short.mp4")
if clip2.duration > clip1.duration:
    clip2 = clip2.subclip(0, clip1.duration)
    

    
#check clip2 duration
# print('Clip2 duration w.r.t Clip1 duration: ', str(clip2.duration))



















# clip = clip.subclip(0, 5)
  
# getting clip size
# clip = clip.subclip(0, 5)
# print('duration: ',  str(clip.duration))
# printing size
# print("Clip Size ", end = " : ")
# print(value)