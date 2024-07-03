'''import os
import shutil

path = input ("Enter Path: ")
files = os.listdir(path)
for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    if os. path.exists(path+'/'+extension) :
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file) 
    else:
        os. makedirs (path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)'''

import os, shutil
path = input ("Enter Path: ")

file_name = os.listdir(path)

folder_names = ['pdf', 'images', 'videos', 'app', 'zip', 'music']
x = len(folder_names)
for loop in range(0,x):
    if not os.path.exists(path + '/' + folder_names[loop]):
        #print(path + folder_names[Loop])
        os.makedirs(path + '/' + folder_names[loop])

for file in file_name:
    #pdf
    if ".pdf" in file and not os.path.exists(path + "/pdf/" + file): 
        shutil.move(path + '/' + file, path + "/pdf/" + file)
    #images
    elif ".jpg" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".JPG" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".png" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".jpeg" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".jp2" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".heic" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    elif ".HEIC" in file and not os.path.exists(path + "/images/" + file):
        shutil.move(path + '/' + file, path + "/images/" + file)
    #videos
    elif ".mkv" in file and not os.path.exists (path + "/videos/" + file):
        shutil.move(path + '/' + file, path + "/videos/" + file)
    elif ".mp4" in file and not os.path.exists (path + "/videos/" + file):
        shutil.move(path + '/' + file, path + "/videos/" + file)
    elif ".mov" in file and not os.path.exists (path + "/videos/" + file):
        shutil.move(path + '/' + file, path + "/videos/" + file)
    #app
    elif ".dmg" in file and not os.path.exists (path + "/app/" + file):
        shutil.move(path + '/' + file, path + "/app/" + file)
    #zip
    elif ".zip" in file and not os.path.exists (path + "/zip/" + file):
        shutil.move(path + '/' + file, path + "/zip/" + file)
    #music
    elif ".mp3" in file and not os.path.exists (path + "/music/" + file):
        shutil.move(path + '/' + file, path + "/music/" + file)
    