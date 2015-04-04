import os, time, string
from datetime import datetime
from subprocess import *
# Run the command sudo apt-get install inxi
# python3

def robot(text):
    os.system("espeak ' " + text + " ' ")

robot("hello")
while True:
    robot("enter a command")
    command = input("enter a command ")
    words = command.split(' ')
    if ("time") in words:
        time = datetime.now().strftime('%H:%M')
        robot("The time is " + time)
    elif ("update") in words:
        os.system("sudo apt-get update")
    elif ("terminal") in words:
        robot("would you like to launch a virtual terminal or LXterminal? LXTerminal is still in development. 1 or 2")
        thingycommand = input()
        if thingycommand == "1":
            termcommand = input(">>> ")
            os.system(termcommand)
        if thingycommand == "2":
            os.system("lxterminal")
    elif ("meow") in words:
        robot("Virtual Cat. Meow.")
    elif ("easter") in words and ("egg") in words:
        robot("This is not the easter egg")
    elif ("weather") in words:
        #p = subprocess.Popen(['inxi', '-w'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #out, err = p.communicate()
        #a = os.system("inxi -w")
        #a = str(a)
        output = Popen(["inxi", "-w", "-c 0"], stdout=PIPE).communicate()[0]
        #output = str(output)
        print(output)
    elif ("quit") in words:
        break
    elif ("shutdown") in words:
        os.system("sudo shutdown -h now")
    else:
        robot("The command " + command + " is unknown")
