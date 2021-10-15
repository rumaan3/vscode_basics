import os

req_path= input("enter the path ")

if os.path.isfile(req_path):
 print('directory exists')

else : 
  print("wrong path")
  print (os.listdir(req_path))
  all_f_ds=os.listdir(req_path)
  if len(all_f_ds)==0:
     print('path is empty')
  else:
   req_ext=input('enter the required extension:-') 
   req_files=[]
   for each_f in all_f_ds:
     if each_f.endswith(req_ext):
      req_files.append(each_f)
  print(req_files)
  
     