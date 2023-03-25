import os

folder_path = os.path.expanduser("./uploads/gameclips")
filenames = [filename for filename in os.listdir(folder_path)
             if os.path.isfile(os.path.join(folder_path, filename))]
# print(filenames)

for i in filenames:
    parts = i.split('.')
    video_name = parts[0]
    print(video_name)

