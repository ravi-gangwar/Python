import os
#all methods of os module
print("Current working directory: {0}".format(os.getcwd()))
print("-----------------------------------------------------------")
print("List of files and directories: {0}".format(os.listdir()))
print("-----------------------------------------------------------")
print("List of files and directories: {0}".format(os.listdir(os.getcwd())))


os.mkdir("new_dir")
os.rmdir("new_dir")