import os
import glob

# trying to figure out what the right way to get to git-info.js is.
print(glob.glob(os.getcwd()))

input_source = "git-info.js"
print("current working directory:",os.getcwd())
output_dest = "aaa-git-info.js"
print("renaming")
os.rename(input_source,output_dest)
print("finished")