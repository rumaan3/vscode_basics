import os
import shutil



path='C:\\Users\\Rumaan\\Downloads'
exe='C:\\Users\\Rumaan\\Downloads\\applications'
images='C:\\Users\\Rumaan\\Downloads\\images'
zipf='C:\\Users\\Rumaan\\Downloads\\zip_files'
docs='C:\\Users\\Rumaan\\Downloads\\documents'



f=os.listdir(path)

for each in f:
        if each.endswith(".exe"):
            print(len.each)
            shutil.move(os.path.join(path,each),exe)
        if each.endswith(".jpg") or each.endswith(".jpeg") or each.endswith(".png") or each.endswith(".JPG"):
            shutil.move(os.path.join(path,each),images)
        if each.endswith(".zip") or each.endswith(".rar") or each.endswith(".gif") :
            shutil.move(os.path.join(path,each),zipf)
        if each.endswith(".docx") or each.endswith(".xlsx") or each.endswith(".pdf") or each.endswith(".TXT") or each.endswith(".pptx") :
            shutil.move(os.path.join(path,each),docs)
