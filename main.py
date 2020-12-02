import os
import sys

dir_path = input("Enter the path : ")
subfolders = [f.path for f in os.scandir(dir_path) if f.is_dir()]

extensions = ('.mp3', '.flac')

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(extensions):
            print(str(file))