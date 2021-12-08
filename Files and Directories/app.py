from builtins import print
from pathlib import Path

# Absolute Path is root Hadd Disk or Any were
# C:\mo\lk\note.txt ,  D:\

# Relative Path is  Current Directorey
# note.txt

path = Path("folder")
print(path.exists())  # folder is here print True not Show False

path = Path("email")
print(path.exists())  # email folder is here  True not SHow False

path = Path("mead in python")
#path.mkdir() # make Folder
#path.rmdir()  # Remove Folder

path = Path()
for file in path.glob('*'):
    print(file)


