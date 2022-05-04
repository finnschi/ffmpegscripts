import os
import subprocess
import sys
from pathlib import Path


## take first argument as input file

try:
    droppedFile = sys.argv[1]
except IndexError:
    print("No file dropped")

## pathing, filename, etc..
print("your input path is: " + droppedFile)
fileName = os.path.basename(droppedFile)
print("your input filename is: " + fileName)
clipName = os.path.splitext(fileName)[0]
print("your clipName is: " + clipName)
fileDirectory = os.path.dirname(droppedFile)
print("your rootFolder is: " + fileDirectory)

encodesFolder = (clipName + "_website_encodes/")
encodesFolderScrub = (encodesFolder + "scrubbing/" )

outputH264 = (fileDirectory + '/' + encodesFolder + clipName + "_h264.mp4")
outputVp9 = (fileDirectory + '/' + encodesFolder + clipName + "_vp9.webm")
outputWebp = (fileDirectory + '/' + encodesFolderScrub + clipName + "_webP.%04d.webp")
print("Output 1> h264 goes here: " + outputH264)
print("Output 2> VP9 goes here: " + outputVp9)
print("Output 2> VP9 goes here: " + outputWebp)

encodesPath = (fileDirectory + '/' + encodesFolder)

# Check whether the render path exists or not
isExist = os.path.exists(encodesPath)
if not isExist:
    # create folder if doesnt exist
    os.makedirs(encodesPath)
    os.makedirs(encodesPath + "scrubbing/" )
    print("The Render Directory " + encodesPath + "/scrubbing is created!")

# set FFMPEG arguments

ffmpeg_args = {
    "droppedFile": droppedFile,
    "outputH264": outputH264,
    "outputVp9": outputVp9,
    "outputWebp": outputWebp
}
print(ffmpeg_args)
print("START ENCODE")
ffmpeg_command = (
    'ffmpeg -i "{droppedFile}" -c:v libx264 -crf 18 -vf scale="min(1920\,iw)":-2 -preset slow -c:a aac -ar 48k -b:a 256k '
    '"{outputH264}" -y '
    '-c:v libvpx-vp9 -vf scale="min(1920\,iw)":-2 -b:v 8000K -threads 8 -speed 1 '
    '-tile-columns 6 -frame-parallel 1 '
    '-g 9999 -aq-mode 0 -c:a libopus -b:a 256k -f webm "{outputVp9}" -y '
    '-c:v libwebp -vf scale=800:-2 -quality 85 -preset photo -compression_level 6 -r 1.3 "{outputWebp}" -y '
)
print("the ffmpeg command is: " + ffmpeg_command)
ffmpeg_str = ffmpeg_command.format(**ffmpeg_args)
print("parsed ffmpeg string is:  " + ffmpeg_str)
os.popen(ffmpeg_str)


