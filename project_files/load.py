# This will give buffer time to the projects files

import os,time
from colorama import Fore, Style
from __LOGO__ import LOGO
# LOADING SCREEN
class load_project:
  def __init__(self):
    self.loading=True
    self.setup_done=False
    self.has_ip = False
  def _load_(self):
    while self.loading:
      print(Fore.GREEN+Style.BRIGHT+'\n\nSetting Up--[......................]--\n\n')
      time.sleep(0.2)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[#.....................]-- 1%\n\n')
      time.sleep(0.8)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[##....................]-- 2%\n\n')
      time.sleep(0.1)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[####..................]-- 15%\n\n')
      time.sleep(0.4)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[#######...............]-- 30%\n\n')
      time.sleep(0.2)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[###########...........]-- 48%\n\n')
      time.sleep(0.6)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[#################.....]-- 68%\n\n')
      time.sleep(0.8)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[####################..]-- 88%\n\n')
      time.sleep(0.4)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[#####################.]-- 98%\n\n')
      time.sleep(0.2)
      os.system('clear')
      LOGO()
      print('\n\nSetting Up--[######################]-- 100%\n\n')
      #os.system('pip install replace_shell')
      loaded = open('file_loaded','w')
      loaded.write('STATUS_ALERT: loaded')
      loaded.close()
      self.loading=False
def load():
  l = load_project()
  l._load_()
  return
