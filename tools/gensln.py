import subprocess 
import globals

if globals.IsWindows():
    subprocess.call(["cmd.exe", "/c", "premake\\premake5", "vs2019"])

if globals.IsLinux():
   subprocess.call(["premake/premake5Linux.tar","gmake2"])

if globals.IsMac():
    subprocess.call(["premake/premake5Mac.tar", "gmake2"])
    subprocess.call(["premake/premake5Mac.tar", "xcode4"])