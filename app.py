from flask import Flask, request, render_template, send_from_directory,jsonify, redirect, url_for
import os
import datetime
from moviepy.editor import *
from moviepy.video.fx.all import *

app = Flask(__name__,static_folder='static')

app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MEDIA_FOLDER"] = "static" #newly created videos

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/")
def index():
    folder_path = os.path.expanduser("./uploads/gameclips")
    filenames = [filename for filename in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, filename))]
    
    success_message = request.args.get('success')
    video_filename = request.args.get('video')
    
    return render_template('index.html', gameclips=filenames, success=success_message, video=video_filename)
    # return render_template("index.html", gameclips=filenames, testname=testname)

@app.route('/uploadfile',   methods=["POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected.')
        file = request.files['file']
        clip2name = request.form['secfiles']

        # No selected file
        if file.filename == '':
            return render_template('index.html', error='No file selected.')
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        clip1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        clip1 = VideoFileClip(clip1_path)    
        if clip1.duration > 60:
            clip1 = clip1.subclip(0,60) 
    
        clip2= VideoFileClip("uploads/gameclips/"+clip2name)
        if clip2.duration > clip1.duration:
            clip2 = clip2.subclip(0, clip1.duration)
        
        # Double the width of the clip
        # Resize the clip to the new size while maintaining the aspect ratio

        tr1 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","top"))
        tr2 = ImageClip("fondo.png").set_duration(clip1.duration).set_position(("center","bottom"))

        # clip1 = clip1.crop(x1=506, y1 = 0, x2=0, y2 = 900)
        wx = clip1.w
        new_w = 2 * wx
        clip1 = clip1.resize(width=new_w)

        w = clip2.w 
        new_w = 3 * w
        clip2 = clip2.resize(width=new_w)
        w, h = clip2.size
        new_h = h * 1.5
        clip2 = clip2.resize(height=new_h)

        combine = clips_array([[tr1],[clip1],[clip2],[tr2]])

        ts = datetime.datetime.now().timestamp()
        filename = str(ts)+".mp4"

        output_path = os.path.join(app.config['MEDIA_FOLDER'], filename)
        temp_audio_path = os.path.join(app.config['MEDIA_FOLDER'], str(ts)+'.mp3')
        combine.write_videofile(output_path, temp_audiofile=temp_audio_path)
        combine.close()
        # return render_template('index.html', success='Video '+filename+' created', video=filename)
        success_message = f'Video {filename} created'
        return redirect(url_for('index', success=success_message, video=filename))

        # return render_template('index.html', error='Invalid file format. Please upload an MP4 file.')

    return redirect(url_for('index', error='Invalid request'))


if __name__ ==  "__main__":
    app.run(debug=True)
