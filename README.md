# Merge For Shorts

![py_shorts](https://user-images.githubusercontent.com/59218902/220019042-11662e84-01d3-4993-ae03-76274bd76a2c.jpg)


Creating Vertical fit videos using MoviePy 

Sepcial thanks to reddit user [u/ximo23](https://www.reddit.com/user/ximo23).

## Example
- Check out this youtube video : https://www.youtube.com/shorts/vQst9hvQXKI
- `Family Guy` video at the top and `quake` video at the bottom

## screenshot

![Screenshot from 2023-02-17 08-45-19](https://user-images.githubusercontent.com/59218902/219540734-ae55d412-5374-4cb9-9199-e2b3be4a20ca.png)


# Requirements
- This requires `python 3.x`

# Installation
 - Install  dependencies :  `pip install -r requirements.txt`

# Usage

- To run the Flask application, you can use the following command:
```
python app.py 
```

- This will start the Flask development server and you can access the application by visiting http://localhost:5000 in your web browser.

- The format of the video is any movie or tv series clip at the top and random videogame or life hacks videos at the bottom.

- The application allows users to upload an video file which sits at the top and video game at the bottom which is in the `uploads` folder - `quake_short.mp4` , where two of them are combined to form a single video file which is <= `1 minute`. If the video uploaded by the user is greater than a minute it will be reduced to a minute. The progress can be seen on the terminal.  


# Configuration

- You can configure the application by modifying the config dictionary in the `app.py` file. You can set the location and name of the folder where uploaded files will be saved, as well as the maximum allowed file size.

## Contributors

- [jp](https://github.com/pj8912)

# License
This project is licensed under the Apache License Version 2.0.

# Contribution

 The goal of this app is to automate the process of making vertical `shorts` videos of a certain kind. Contributions are always welcome, no matter how large or small. Pull requests are always welcome, and I'll do my best to do reviews as fast as I can. 

In the case of a bug report, bugfix or a suggestions, please feel very free to open an issue too.



# :heart: Support me by donating

Hi there! If you've found my work helpful or useful in any way, please consider supporting me by donating. Your support helps me continue to create and share useful projects with the community. Thank you for your generosity and support! :handshake:


<a href="https://www.buymeacoffee.com/gjohnpinto" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
