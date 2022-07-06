import shutil
import os
from datetime import datetime

pathname = input("Enter the path to the directory in which you want to rename all the files ")
now = datetime.now()
current_time = now.strftime("%d-%m-%y--%H-%M-%S--")

files = os.listdir(pathname)

print(pathname + "\\")

[(shutil.copyfile(pathname + "\\" + filename, pathname + "\\" + current_time + filename)) and (os.remove(pathname +
     "\\" + filename)) for filename in files if "." in filename]
