import subprocess, os, pyfiglet, sys
from time import *
subprocess.run("pip install -r requirements.txt".split())
os.system("clear")

def logo():
  print("""
\t _  __          _             ____            _                  _
\t| |/ /__ _ _ __(_)_ __ ___   | __ )  __ _  __| | ___  _   _ _ __(_)
\t| ' // _` | '__| | '_ ` _ \  |  _ \ / _` |/ _` |/ _ \| | | | '__| |
\t| . \ (_| | |  | | | | | | | | |_) | (_| | (_| | (_) | |_| | |  | |
\t|_|\_\__,_|_|  |_|_| |_| |_| |____/ \__,_|\__,_|\___/ \__,_|_|  |_|

\tTelegram : @UltraCode000
\tWhatsApp : +21652685817""")
  
def main():
  subprocess.run("python ./bot.py".split())
  
def control():
  try:
    logo()
    main()
  except KeyboardInterrupt:
    print("\n[!] CTRL+C Exiting . . .")
    sleep(2)
    sys.exit()
if __name__ == '__main__':
  control()
