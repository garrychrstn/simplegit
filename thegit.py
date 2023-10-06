import subprocess
from colorama import init, Fore

init()

cmd = " "
option = " "
def command(option):
    option = input("what do you wanna do : \n1. Status\n2. Add\n3. Commit\n4. Push \n5. Exit\noption: ")
    while option != '5':
        if option == '1':
            cmd = "git status *"
            return cmd
        if option == '2':
            cmd = "git add *"
            return cmd
        if option == '3':
            cm = input("Commit message : ")
            cmd = f"git commit -m '{cm}'"
            return cmd
        if option == '4':
            dst = input("repository destination : ")
            brc = input("branch : ")
            cmd = f"git push {dst} {brc}"
            return cmd

cmd = command(option)
#This is comment
try:
    print(cmd)
    result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(Fore.GREEN + "Command Output : ")
    print(result.stdout)

    if result.stderr:
        print(Fore.RED + "Command Error : ")
        print(result.stderr)

except subprocess.CalledProcessError as e:
    print(Fore.RED + f"Error executing the command : {e}")
except Exception as e:
    print(Fore.RED + f"Error occured : {e}")
