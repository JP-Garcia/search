from subprocess import Popen, PIPE
from sys import argv

def help():
    print("Search all searchable files line-by-line in current directory, using `find`.")
    print("Prints filepath, line number, and the line itself.")
    print()
    print("Usage: python3 search.py [string]           search for \"string\"")
    print("   or: python3 search.py --help             print help (this message) and exit")

def search(substring):
    print("now looking for:", substring)
    print("-"*40)
    
    arg_list = ["find", "."]
    f = Popen(arg_list, stdin=PIPE, stdout=PIPE, text=True)
    
    out_find = f.stdout.read()
    # print(out_find)
    
    for path in out_find.splitlines():
    
        try:
            file = open(path)
            print(" "*120, end="\r")
            print("searching file:", path[:100], end="\r")
            
            i = 0
            for line in file:
                i += 1
                if substring in line:
                    print(" "*120, end="\r")
                    print(f"{path:55} {i:>8}: {line.strip()}")
        except KeyboardInterrupt:
            print("\n"+"*"*50, "KeyboardInterrupt", "*"*50)
            break
        except (IsADirectoryError, UnicodeDecodeError):
            pass

    print("-"*40)
    print("done")
    f.terminate()


# ====================== main ======================

try:
    arg1 = str(argv[1])
    if arg1 == "--help":
        help()
    else: search(arg1)
except IndexError: 
    help()
