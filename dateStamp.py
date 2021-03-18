import glob
import os
import datetime

print('Enter the path of your files.')
fpath = input()
os.chdir(fpath)

today = datetime.date.today()

for f in glob.glob('*.*'):
    filename, file_extension = os.path.splitext(f)
    os.rename(f, filename + " " + today.strftime('%m%d%y') + file_extension)
