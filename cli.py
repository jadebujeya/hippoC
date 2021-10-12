# cli build
# cli run
# cli gen
# cli version
# cli gen build run

import os, sys
import subprocess

TOOLS_DIR = "tools"

def RunCommand(cmdArg):
    subprocess.call(["python3", "{}/{}/{}.py".format(os.getcwd(), TOOLS_DIR, cmdArg)])

lenVar=len(sys.argv)

for i in range(1, lenVar):
    cmd = sys.argv[i]
    print("\n-------------")
    print("Excecuting: ", cmd)
    RunCommand(cmd)


    