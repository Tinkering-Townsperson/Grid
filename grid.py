import os, sys
file = sys.argv[1]
print("It looks like you tried to open \""+file+"\".")
if not os.system("echo \"%path:; C:\\Program Files (x86)\\Grid\\=%\"") == os.system("\"%path%\""):
    print("YAY!!!")
else:
    os.system("set path=%path%; C:\\Program Files (x86)\\Grid\\")
op = input("""Would you like to open it in:
1. Compile the file(default)
2. Edit the file
""")

if op == "2":
    os.system("gride.exe \""+file+"\"")
else:
    os.system("gridc.exe \""+file+"\"")
