import os
import shutil

#Path of the directory that needs to be organized
path = 'C:/Users/tnage/Desktop/python projects/Organize File'
#Storing all the files and directory in a list of the directory
list_ = os.listdir(path)

#handeling each file of the directory
for file_ in list_:
    name,ext = os.path.splitext(file_)
    #not taking the dot from the extension
    ext = ext[1:]
    #if directory is present not handel it
    if ext == '':
        continue
    #it the extension name directory is already present directory sending the file to the required directory
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)
    #creating the requried directory and sending the file
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file_,path+'/'+ext+'/'+file_)