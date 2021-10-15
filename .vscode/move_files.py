import glob, os
import shutil

req_path='C:\\Users\\Rumaan\\Downloads'


if os.path.isfile(req_path):
 print('directory exists')

else : 
  all_f_ds=os.listdir(req_path)
  if len(all_f_ds)==0:
     print('path is empty')
  else:
      files=glob.glob('*.pdf')
      images=glob.glob('*.jpg')
      print(files)
      print(images)
     # dest=input("enter the destination path")
      #for each_f in all_f_ds:
           
         # if each_f.endswith(docs):
            #  print(each_f)
              
              #shutil.move(os.path.join(req_path,each_f),dest)
    
    #print(os.listdir(dest))

     