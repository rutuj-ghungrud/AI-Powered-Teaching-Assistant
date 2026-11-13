import os
import subprocess

files = os.listdir("videos")
for file in files:
    video_number = file.split(" [")[0].split(" Part")[1]
    file_name = file.split(" - ")[0]
    print(video_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_number}_{file_name}.mp3"])