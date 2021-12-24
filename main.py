import subprocess
import os
subprocess.run("pip install pyfiglet".split())
subprocess.run("pip install python-telegram-bot".split())
os.system("clear")
import pyfiglet

def logo():
  print("""
_  __          _             ____            _                  _
| |/ /__ _ _ __(_)_ __ ___   | __ )  __ _  __| | ___  _   _ _ __(_)
| ' // _` | '__| | '_ ` _ \  |  _ \ / _` |/ _` |/ _ \| | | | '__| |
| . \ (_| | |  | | | | | | | | |_) | (_| | (_| | (_) | |_| | |  | |
|_|\_\__,_|_|  |_|_| |_| |_| |____/ \__,_|\__,_|\___/ \__,_|_|  |_|

\tTelegram : @UltraCode000
\tWhatsApp : +21652685817""")
  
def main():
  logo()
  subprocess.run("python bot.py".split())
  
main()
