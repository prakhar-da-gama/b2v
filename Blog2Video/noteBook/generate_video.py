#Number of Images we have
NumberOfImages = 0
for x in words:
  img_path = "/content/dataset/"+x+"/Image_1.jpg"
  try:
    image = io.imread(img_path)
    NumberOfImages = NumberOfImages + 1
  except:
    print(">")
print(NumberOfImages)
  
Frame_Per_Second = 0
if audioclip_duration != 0:
  #
  Frame_Per_Second = NumberOfImages/audioclip_duration
print(Frame_Per_Second)

import os
import shutil
counter = 0;
for x in words:
  try:

  
    os.rename("/content/dataset/"+x+"/Image_1.jpg", "/content/dataset/"+x+"/"+x+".jpg")
    #os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    #src_path = r"/content/dataset/"+x+"/"+x+".jpg"
    #dst_path = r"/content/images/"+x+"/"+x+".jpg"
    #shutil.move(src_path, dst_path)
  except:
    print("no")

import os
import shutil
for x in words:
  try:

  
    
    #os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
    src_path = r"/content/dataset/"+x+"/"+x+".jpg"
    dst_path = r"/content/images/"+x+".jpg"
    shutil.move(src_path, dst_path)
  except:
    print("no")


import os
import shutil
counter = 0;
for x in words:
  counter = counter + 1;
  try:

  
    os.rename("/content/images/"+x+".jpg", "/content/images/"+str(counter)+".jpg")
    
  except:
    print("no")


# importing libraries
import os
import cv2
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
#os.chdir("C:\\Python\\Geekfolder2")
path = "/content/images"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir(path))
print(num_of_images)

for file in os.listdir(path):
	im = Image.open(os.path.join(path, file))
	width, height = im.size
	mean_width += width
	mean_height += height
	# im.show() # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

from moviepy.editor import AudioClip

# importing libraries
import os
import cv2
from PIL import Image

# Checking the current directory path
print(os.getcwd())

# Folder which contains all the images
# from which video is to be generated
os.chdir("/content/images")
path = "/content/images"

mean_height = 0
mean_width = 0

num_of_images = len(os.listdir('.'))
# print(num_of_images)

for file in os.listdir('.'):
	im = Image.open(os.path.join(path, file))
	width, height = im.size
	mean_width += width
	mean_height += height
	# im.show() # uncomment this for displaying the image

# Finding the mean height and width of all images.
# This is required because the video frame needs
# to be set with same width and height. Otherwise
# images not equal to that width height will not get
# embedded into the video
mean_width = int(mean_width / num_of_images)
mean_height = int(mean_height / num_of_images)

# print(mean_height)
# print(mean_width)

# Resizing of the images to give
# them same width and height
for file in os.listdir('.'):
	if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith("png"):
		# opening image using PIL Image
		im = Image.open(os.path.join(path, file))

		# im.size includes the height and width of image
		width, height = im.size
		print(width, height)

		# resizing
		imResize = im.resize((mean_width, mean_height), Image.ANTIALIAS)
		imResize.save( file, 'JPEG', quality = 95) # setting quality
		# printing each resized image name
		print(im.filename.split('\\')[-1], " is resized")


# Video Generating function
def generate_video():
	image_folder = '.' # make sure to use your folder
	video_name = 'mygeneratedvideo.avi'
	os.chdir("/content/images")
	
	images = [img for img in os.listdir(image_folder)
			if img.endswith(".jpg") or
				img.endswith(".jpeg") or
				img.endswith("png")]
	
	# Array images should only consider
	# the image files ignoring others if any
	print(images)

	frame = cv2.imread(os.path.join(image_folder, images[0]))

	# setting the frame width, height width
	# the width, height of first image
	height, width, layers = frame.shape

	video = cv2.VideoWriter(video_name, 0, Frame_Per_Second, (width, height))

	# Appending the images to the video one by one
	for image in images:
		video.write(cv2.imread(os.path.join(image_folder, image)))
	
	# Deallocating memories taken for window creation
	cv2.destroyAllWindows()
	video.release() # releasing the video generated


# Calling the generate_video function
generate_video()

# Import everything needed to edit video clips
#Combining the audio and the Images to make a video clip


# loading video dsa gfg intro video
clip = VideoFileClip("mygeneratedvideo.avi")


# getting only first 5 seconds
#clip = clip.subclip(0, 5)

# loading audio file
audioclip = AudioFileClip("/content/AudioClip.mp3")

# adding audio to the video clip
video_clip = clip.set_audio(audioclip)

video_clip.duration = audioclip.duration
# set the FPS to 1
video_clip.fps = 1
# write the resuling video clip
video_clip.write_videofile("Video_with_audio.mp4")

# showing video clip
video_clip.ipython_display()
