import os
import sys
import datetime
today=datetime.datetime.now()
path=input('enter path:-')
if not os.path.exists(path):
 print('does not exist:-')
 sys.exit(1)
if os.path.isfile(path):
 print('path is a file')
 sys.exit(2)

all_f=os.listdir(path)

for each in all_f :
 each_p=os.path.join(path,each)
 if os.path.isfile(each_p):
     each_fd=datetime.datetime.fromtimestamp(os.path.getctime(each_p))
     print(each_p,(today-each_fd).days)
  
