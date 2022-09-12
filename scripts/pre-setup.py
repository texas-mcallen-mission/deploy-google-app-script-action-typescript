import os
import shutil
print("setting things up.")

checklist = """
Things to check for:

Does clasp.json exist yet?

Does git-info.js (or TS?) exist yet?  - if not, copy over local version

Does .claspignore exist yet? - if not, create a file, and put /deploy-data in it
    - also just pipe in deploy-data/ in there, it really doesn't matter if it's there twice

Could also stick an empty .gs file in there as a watermark, lol?

Basically I need to find *everything* necessary to make an empty repo and push it and make a local, basic copy.
"""

claspIg = ".claspignore"
deployDataLine = "deploy-data/**"

files = [".clasp.json", "git-info.js", "tsconfig.json", "appsscript.json", claspIg]

addedFiles = []


reqFileDir = "deploy-data/required-files/"

for entry in files:
    if os.path.exists(entry) == False and os.path.exists(reqFileDir+entry) == True:
        shutil.copy2(reqFileDir+entry, entry)
        addedFiles.append(entry)


# then run code to modify claspignore?
if addedFiles.count(claspIg) == 0:  # this is like array.includes, I guess?
    # pipe thingies in
    print("modifying"+claspIg)
    claspIgnoreFile = open(claspIg, mode="r+")
    print("pre-mod:", claspIgnoreFile.read())
    print(deployDataLine, file=claspIgnoreFile) # adds newline
    claspIgnoreFile.close()


if len(addedFiles) > 0:
    # spread operator thingy to get rid of the brackets.  Super neat!
    print("Completed- added ", *addedFiles)
else:
    print("Completeted, no new files added.")

