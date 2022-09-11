import os
import shutil
print("placeholder ATM")

checklist = """
Things to check for:

Does clasp.json exist yet?

Does git-info.js (or TS?) exist yet?  - if not, copy over local version

Does .claspignore exist yet? - if not, create a file, and put /deploy-data in it
    - also just pipe in deploy-data/ in there, it really doesn't matter if it's there twice

Could also stick an empty .gs file in there as a watermark, lol?

Basically I need to find *everything* necessary to make an empty repo and push it and make a local, basic copy.
"""

claspJsonPath = "clasp.json"

reqFileDir = "deploy-data/required-files/"

if os.path.exists(claspJsonPath) == False:
    shutil.copy2(claspJsonPath,reqFileDir+claspJsonPath)

gitInfo_path =  "git-info.js"
if os.path.exists(gitInfo_path) == False:
    shutil.copy2(gitInfo_path,reqFileDir+gitInfo_path)

