
import os, glob
 
dir = 'static/csv'
filelist = glob.glob(os.path.join(dir, "*"))
for f in filelist:
    os.remove(f)