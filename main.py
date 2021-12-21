GNU nano 6.0                        main.py
import subprocess
import os
subprocess.run("pip install pyfiglet".split())
os.system("clear")
import pyfiglet
print(pyfiglet.figlet_format("Karim Badouri"))

subprocess.run("python ./telegram/bot.py".split())
