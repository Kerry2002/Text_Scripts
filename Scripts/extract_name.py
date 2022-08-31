import os

a = open(r"C:\Users\DM\Desktop\830\python.txt", "w",encoding='utf-8')
for path, subdirs, files in os.walk(r"C:\Users\DM\Desktop\ALL_20220819"):
   for filename in files:
      a.write(filename.split('.')[0]+ '\n')