#!/usr/bin/env python
import os.path
import datetime

# Move contents of downloads folder into archive folder named with yesterday's date
# If yesterday's folder already exists, do nothing. 

def main():
  # Get path to downloads archive folder and create if needed 
  sDownloadsFolder=os.path.expanduser("~/dloads") 
  sDownloadsArchiveFolder = os.path.join(sDownloadsFolder,'__archive')
  if not os.path.exists(sDownloadsArchiveFolder):
    os.mkdir(sDownloadsArchiveFolder)
  
  # Get path to archive folder
  dtYesterday=datetime.datetime.now() - datetime.timedelta(days=1)
  sYesterday=dtYesterday.strftime('__%Y-%m-%d')
  sNewArchiveFolder = os.path.join(sDownloadsArchiveFolder, sYesterday)
  if os.path.exists(sNewArchiveFolder):
    return
  os.mkdir(sNewArchiveFolder)
  
  # List downloads folder and move everything except '=archive'
  os.chdir(sDownloadsFolder)
  lFilesToMove = os.listdir()
  for f in lFilesToMove:
    if f == '__archive':
      continue
    os.rename(f, os.path.join("__archive", sYesterday, f))
  return

if __name__ == '__main__':
  main()
