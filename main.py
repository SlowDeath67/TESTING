import subprocess
import os
subprocess.run("pip install -r requirements.txt".split())
os.system("clear")
import pyfiglet

def logo():
  print("""
\t_  __          _             ____            _                  _
\t| |/ /__ _ _ __(_)_ __ ___   | __ )  __ _  __| | ___  _   _ _ __(_)
\t| ' // _` | '__| | '_ ` _ \  |  _ \ / _` |/ _` |/ _ \| | | | '__| |
\t| . \ (_| | |  | | | | | | | | |_) | (_| | (_| | (_) | |_| | |  | |
\t|_|\_\__,_|_|  |_|_| |_| |_| |____/ \__,_|\__,_|\___/ \__,_|_|  |_|

\tTelegram : @UltraCode000
\tWhatsApp : +21652685817""")
  
def main():
  logo()
  subprocess.run("python ./bot.py".split())
  
main()
