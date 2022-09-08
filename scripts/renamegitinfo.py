import os

input_source = "/git-info.js"

output_dest = "/aaa-git-info.js"
print("renaming")
os.rename(input_source,output_dest)
print("finished")
