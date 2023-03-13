# trim video code 

from moviepy.editor import *

clip = VideoFileClip("/home/pi/autonomus_robo/123.mp4").subclip(7,42)
clip.write_videofile("/home/pi/autonomus_robo/123_t.mp4")