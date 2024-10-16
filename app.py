from flask import Flask, request, render_template, send_from_directory,jsonify, redirect, url_for
import os
import datetime
from moviepy.editor import *
from moviepy.video.fx.all import *
# from moviepy.video.fx.all import crop
import proglog
# import tqdm 
from tqdm import tqdm


app = Flask(__name__,static_folder='static')

app.config["UPLOAD_FOLDER"] = "uploads" #uploaded files saved at uploads/ and then take for processing
app.config["MEDIA_FOLDER"] = "static" #newly created videos


##

#about page
@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/merge', endpoint='merge')
def merge_page():
    folder_path = os.path.expanduser("./uploads/gameclips")
    filenames = [filename for filename in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, filename))]
    
    success_message = request.args.get('success')
    video_filename = request.args.get('video')
    
    return render_template('merge.html', gameclips=filenames, success=success_message, video=video_filename)

# home page
@app.route("/", endpoint='index')
def index():
    folder_path = os.path.expanduser("./uploads/gameclips")
    filenames = [filename for filename in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, filename))]
    
    success_message = request.args.get('success')
    video_filename = request.args.get('video')
    
    return render_template('index.html', gameclips=filenames, success=success_message, video=video_filename)



@app.route('/altmerge', methods=['POST'])
def altmerge():
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
        if clip1.duration > 10:
            clip1 = clip1.subclip(0,10)
        (wx, hx) = clip1.size
        if wx != 1920 and hx !=1080:
            clip1 = clip1.resize(width=1920,height=1080)
    
        clip2= VideoFileClip("uploads/gameclips/"+clip2name)
        if clip2.duration > clip1.duration:
            clip2 = clip2.subclip(0, clip1.duration)
        (wy, hy) = clip2.size
        if wy != 1920 and hy !=1080:
            clip2 = clip2.resize(width=1920,height=1080)
        
    
        combine = clips_array([[clip1],[clip2]])
        # combine = clips_array([[clip1],[clip2]])


        ts = datetime.datetime.now().timestamp()
        filename = str(ts)+".mp4"

        output_path = os.path.join(app.config['MEDIA_FOLDER'], filename)
        temp_audio_path = os.path.join(app.config['MEDIA_FOLDER'], str(ts)+'.mp3')
        combine.write_videofile(output_path, temp_audiofile=temp_audio_path)
        combine.close()
        
        clip = VideoFileClip(output_path)
        (w, h) = clip.size
        cropped_clip = crop(clip, width=550, height=6000) #without x and y divided
        new_filname = "crop_shorts_"+filename
        new_path =os.path.join(app.config['MEDIA_FOLDER'], new_filname)
        cropped_clip.write_videofile(new_path,codec="libx264")
        
    
        # return render_template('index.html', success='Video '+filename+' created', video=filename)
        success_message = f'Video {filename} created'
        return redirect(url_for('index', success=success_message, video=filename))
    return redirect(url_for('index', error='Invalid request'))

# shorts page
@app.route('/shorts')
def shorts_page():
    success_message = request.args.get('success')
    video_filename = request.args.get('video')
    return render_template('crop.html', success=success_message, video=video_filename)

 
#first function 
@app.route('/croptoshorts', methods=['POST'])
def crop_to_shorts():
    if request.method == "POST":
        if 'file' not in request.files:
            return render_template('index.html', error='No file selected.')
        file = request.files['file']
        
        # No  file selected
        if file.filename == '':
            return render_template('index.html', error='No file selected.')
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        clip1_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)


        # creating new filename
        ts = datetime.datetime.now().timestamp()
        filename = str(ts)+".mp4"
        filename="crop_short_"+filename
        output_path = os.path.join(app.config['MEDIA_FOLDER'], filename)

        # ffmpeg command line [NEW]
        os.system(f'ffmpeg -i {clip1_path} -filter:v "crop=in_h*9/16:in_h" -c:a copy {output_path}')
     
        # moviepy [old]

        # temp_audio_path = os.path.join(app.config['MEDIA_FOLDER'], str(ts)+'.mp3')
        
        # clip = VideoFileClip(clip1_path)
        # # clip for 10 sec
        # if clip.duration > 10:
        #     clip = clip.subclip(0,10)
        # (w, h) = clip.size
        # if w != 1920 and h !=1080:
        #     clip = clip.resize(width=1920,height=1080)
        # bar = tqdm(total=clip.duration)
        # cropped_clip = crop(clip, width=500, height=5000, x_center=w/1.5, y_center=h/1.5)
        # cropped_clip.write_videofile(output_path,codec="libx264",temp_audiofile=temp_audio_path)
        
        success_message = f'Video {filename} created'
        return redirect(url_for('shorts_page', success=success_message, video=filename))
    else:
        return redirect(url_for('shorts_page', error='Invalid request'))




if __name__ ==  "__main__":
    app.run(debug=True)
