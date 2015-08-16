#-*- coding:utf-8 -*-

import win32com.client
import os
import subprocess
import time

command = 'taskkill /F /IM Config.exe'
file = r"D:\game\Dynasty Warriors 8 - Empires\Config.exe"

def check_exsit(process_name):
  try:
    WMI = win32com.client.GetObject('winmgmts:') 
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
  except Exception,e:
    print process_name + "error : ", e
  if len(processCodeCov) > 0:
    print process_name + " exist"
    return True
  else:
    print process_name + " is not exist"
    return False
    
if __name__ == '__main__':
	i = 0
	while i<100:
		if check_exsit('Config.exe'):
			os.system(command)
		else:
			subprocess.Popen(file)
		time.sleep(1)
		i = i+1
