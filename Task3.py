import os
import shutil

files = os.listdir(r"C:\downloads\ahmed\ahmed\media")

for file in files:
    if file.endswith(".jpg") or  file.endswith(".png"):
        sourcePath = os.path.join(r"C:\downloads\ahmed\ahmed\media", file)
        destinationPath = os.path.join(r"C:\Users\Me Rah\Documents", file)
        shutil.move(sourcePath, destinationPath)
        
