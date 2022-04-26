import os, sys
file = sys.argv[1]
print("It looks like you tried to open \""+file+"\".")
op = input("""Would you like to open it in:
1. Compile the file(default)
2. Edit the file
""")

if op == "2":
    os.system("'C:\\Program Files (x86)\\Grid\\gride.exe' '"+file+"'")
else:
    os.system("'C:\\Program Files (x86)\\Grid\\gridc.exe' '"+file+"'")
