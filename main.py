import subprocess
import os
subprocess.run("pip install pyfiglet".split())
os.system("clear")
print(pyfiglet.figlet_format("Karim Badouri"))

subprocess.run("python ./telegram/bot.py")
