# import glob

# files = glob.glob("./JPEGImages/*")
# for file in files:
#     print(file)


import os

path = "./VOCDevkit/VOC2007/JPEGImages/"

f = open('./VOCDevkit/VOC2007/ImageSets/Main/train.txt', 'w')

files = os.listdir(path)
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
# print(files_file)   # ['file1', 'file2.txt', 'file3.jpg'
for filepath in files_file:
    basename_without_ext = os.path.splitext(os.path.basename(filepath))[0]
    print(basename_without_ext)
    f.write(basename_without_ext)
    f.write('\n')

f.close()