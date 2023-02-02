# from moviepy.editor import *
# from moviepy.video.fx.all import *

# mpath = r"C:/Users/joaqu/Desktop/Pruebas/MateriaPrima/Charlando Chill con Javi Ep.X.mp4"
# bpath = r"C:/Users/joaqu/Desktop/Pruebas/MateriaPrima/DIRTY RACER REVENGE! (GTA 5 Instant Karma Moments 28).mp4"
# ap = r"C:/Users/joaqu/Desktop/Pruebas/Aprobacion previa/ultimo.mp4"

# clipJAVI = VideoFileClip(mpath).subclip("0:43:09","0:44:09").fx(afx.audio_normalize)
# clipGTA = VideoFileClip(bpath, audio=False).subclip("0:02:09","0:03:09")

# arriba = ImageClip("fondo.png").set_duration(clipJAVI.duration).set_position(("center","top"))
# abajo = ImageClip("fondo.png").set_duration(clipJAVI.duration).set_position(("center","bottom"))

# w,h = clipJAVI.size

# clipJAVI = clipJAVI.crop(x1=640, y1 = 0, x2=1280, y2 = 360)
# text = TextClip("¿Como ganar GH 2022?", size=(720,100), color="white").set_position(("center","center")).set_duration(10)
# #text3 = TextClip("la produccion de GH", size=(720,100), color="white").set_position(("center",text.h+135)).set_duration(10)
# text2 = TextClip("Parte 1", size=(720,100), color="white").set_position(("center","top")).set_duration(10)

# arribaconTXT = CompositeVideoClip([arriba, text])
# abajoconTXT = CompositeVideoClip([abajo, text2])

combine = clips_array([[arribaconTXT],[clipJAVI],[clipGTA],[abajoconTXT]])
#combine.save_frame("frame.png", t = 1)
combine.write_videofile(ap)
combine.close()