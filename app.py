from flask import Flask, request, render_template, send_from_directory,jsonify
import os
import datetime
from moviepy.editor import *
from moviepy.video.fx.all import *



ts = datetime.datetime.now().timestamp()


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"



@app.route("/")
def index():
    return render_template("index.html")

@app.route('/uploadfile',   methods=["POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected.')

        file = request.files['file']
        if file.filename == '':
        # No selected file
            return render_template('index.html', error='No file selected.')


        # clip1 = VideoFileClip( os.path.join(request.files['file'].filename))
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        clip1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        clip1 = VideoFileClip(clip1_path)
            
        if clip1.duration > 60:
            clip1 = clip1.subclip(0,60) 
    
        clip2 =   VideoFileClip("uploads/quake_short.mp4",audio=False)
        if clip2.duration > clip1.duration:
            clip2 = clip2.subclip(0, clip1.duration)

        tr1 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","top"))
        tr2 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","bottom"))

        clip1 = clip1.crop(x1=506, y1 = 0, x2=0, y2 = 900)
        combine = clips_array([[tr1],[clip1],[clip2],[tr2]])
        ts = datetime.datetime.now().timestamp()
        filename = str(ts)+".mp4"
        combine.write_videofile(filename)
        combine.close()




        # return 'File uploaded successfully!', 200
        return render_template('index.html', success='Video '+filename+' created')

    # File is not an MP4 file
        return render_template('index.html', error='Invalid file format. Please upload an MP4 file.')

    return render_template('index.html', error='Invalid request')


if __name__ ==  "__main__":
    app.run(debug=True)
