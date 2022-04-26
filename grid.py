import os, sys
file = sys.argv[1]
print("It looks like you tried to open \""+file+"\".")
op = input("""Would you like to:
1. Compile the file(default)
2. Edit the file(Work In Progress)
""")

if op == "2":
    os.system("C:\\Grid\\gride.exe "+file)
else:
    os.system("C:\\Grid\\gridc.exe "+file)
