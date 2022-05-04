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

encodesFolder = ("h264/")

outputH264 = (fileDirectory + '/' + encodesFolder + clipName + "_h264.mp4")
print("Output 1> h264 goes here: " + outputH264)

encodesPath = (fileDirectory + '/' + encodesFolder)

# Check whether the render path exists or not
isExist = os.path.exists(encodesPath)
if not isExist:
    # create folder if doesnt exist
    os.makedirs(encodesPath)
    print("The Render Directory " + encodesPath + "/scrubbing is created!")

# set FFMPEG arguments

ffmpeg_args = {
    "droppedFile": droppedFile,
    "outputH264": outputH264
}
print(ffmpeg_args)
print("START ENCODE")
ffmpeg_command = (
    'ffmpeg -i "{droppedFile}" -c:v libx264 -crf 18 -preset slow -c:a aac -ar 48k -b:a 256k '
    '"{outputH264}" -y '
)
print("the ffmpeg command is: " + ffmpeg_command)
ffmpeg_str = ffmpeg_command.format(**ffmpeg_args)
print("parsed ffmpeg string is:  " + ffmpeg_str)
os.popen(ffmpeg_str)


