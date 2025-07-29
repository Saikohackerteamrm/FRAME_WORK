#!/usr/bin/env python3
# TEAM S-H-T Hacking Framework (Fixed v0.2)
# Author: TEAM S-H-T | RM Rony Ali (Saiko)

import os, sys
from time import sleep as timeout

# ---------- ADVANCE SYSTEM FUNCTION ----------
def clear():
    os.system("clear")

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def install(pkg):
    os.system(f"pkg install {pkg} -y")

def clone_tool(repo):
    name = repo.split("/")[-1].replace(".git", "")
    if not os.path.exists(name):
        os.system(f"git clone {repo}")
    return name

# ---------- TOOLS FUNCTIONS (AUTO INSTALL + RUN) ----------

# -- Information Gathering --
def nmap():
    install("nmap")
    target = input("[?] Target IP or Domain: ")
    os.system(f"nmap -sV {target}")
    timeout(2)

def red_hawk():
    install("php")
    name = clone_tool("https://github.com/Tuhinshubhra/RED_HAWK.git")
    os.system(f"php {name}/rhawk.php")

def dtect():
    name = clone_tool("https://github.com/shawarkhanethicalhacker/D-TECT-1.git")
    os.system(f"python2 {name}/d-tect.py")

def sqlmap():
    install("python")
    name = clone_tool("https://github.com/sqlmapproject/sqlmap.git")
    os.system(f"python3 {name}/sqlmap.py --wizard")

def reconDog():
    name = clone_tool("https://github.com/s0md3v/ReconDog.git")
    os.system(f"python3 {name}/dog")

# -- Vulnerability Analysis --
def routersploit():
    install("python")
    name = clone_tool("https://github.com/threat9/routersploit.git")
    os.system(f"python3 {name}/rsf.py")

def androbugs():
    install("python")
    name = clone_tool("https://github.com/AndroBugs/AndroBugs_Framework.git")
    os.system(f"python3 {name}/androbugs.py -h")

def wpscan():
    install("ruby")
    os.system("gem install wpscan")
    target = input("[?] Target Website: ")
    os.system(f"wpscan --url {target}")

def sn1per():
    name = clone_tool("https://github.com/1N3/Sn1per.git")
    os.system(f"bash {name}/sniper")

# -- Web Hacking --
def websploit():
    name = clone_tool("https://github.com/websploit/websploit.git")
    os.system(f"python3 {name}/websploit.py")

def xattacker():
    name = clone_tool("https://github.com/Moham3dRiahi/XAttacker.git")
    os.system(f"perl {name}/XAttacker.pl")

def cmseek():
    name = clone_tool("https://github.com/Tuhinshubhra/CMSeeK.git")
    os.system(f"python3 {name}/cmseek.py")

def sublist3r():
    name = clone_tool("https://github.com/aboul3la/Sublist3r.git")
    os.system(f"python3 {name}/sublist3r.py -h")

# -- Database Assessment --
def dbdat():
    name = clone_tool("https://github.com/foospidy/DbDat.git")
    os.system(f"python3 {name}/DbDat.py")

def nosqlmap():
    name = clone_tool("https://github.com/codingo/NoSQLMap.git")
    os.system(f"python3 {name}/nosqlmap.py")

# ---------- MAIN ----------
def main():
    clear()
    print("""
\033[36m
//////////////////////////////////////////////////////////////////////////////
//     _______________    __  ___   _____       __  __    ______           //
//    /_  __/ ____/   |  /  |/  /  / ___/      / / / /   /_  __/          //
//     / / / __/ / /| | / /|_/ /   \__ \______/ /_/ /_____/ /            //
//    / / / /___/ ___ |/ /  / /   ___/ /_____/ __  /_____/ /            //
//   /_/ /_____/_/  |_/_/  /_/   /____/     /_/ /_/     /_/            //
//  Telegram  : @SHT7669            TEAM S-H-T Framework              //
//  Developer : RM Rony Ali         Tools Type: PAID  Version: 0.2   //
//////////////////////////////////////////////////////////////////////

""")
    os.system("xdg-open https://www.facebook.com/profile.php?id=61551487702871")

    print("\033[32m   [01] Information Gathering")
    print("   [02] Vulnerability Analysis")
    print("   [03] Web Hacking")
    print("   [04] Database Assessment")
    print("   [05] Update By TEAM S-H-T\n")
    print("\033[31m   [00] Exit TEAM S-H-T\n")
    rm = input("\033[93mSaiko > Fuck You:- ")

    # Info Gathering
    if rm.strip() in ["1", "01"]:
        clear()
        print("\n[ INFORMATION GATHERING TOOLS ]\n")
        print("    [01] Nmap")
        print("    [02] Red Hawk")
        print("    [03] D-TECT")
        print("    [04] sqlmap")
        print("    [05] ReconDog")
        print("\n    [00] Back\n")
        ch = input("Choose Tool > ")
        if ch in ["1", "01"]: nmap()
        elif ch in ["2", "02"]: red_hawk()
        elif ch in ["3", "03"]: dtect()
        elif ch in ["4", "04"]: sqlmap()
        elif ch in ["5", "05"]: reconDog()
        else: restart_program()

    # Vulnerability Analysis
    elif rm.strip() in ["2", "02"]:
        clear()
        print("\n[ VULNERABILITY ANALYSIS TOOLS ]\n")
        print("    [01] Routersploit")
        print("    [02] AndroBugs Framework")
        print("    [03] WPScan")
        print("    [04] Sn1per")
        print("\n    [00] Back\n")
        ch = input("Choose Tool > ")
        if ch in ["1", "01"]: routersploit()
        elif ch in ["2", "02"]: androbugs()
        elif ch in ["3", "03"]: wpscan()
        elif ch in ["4", "04"]: sn1per()
        else: restart_program()

    # Web Hacking
    elif rm.strip() in ["3", "03"]:
        clear()
        print("\n[ WEB HACKING TOOLS ]\n")
        print("    [01] Websploit")
        print("    [02] XAttacker")
        print("    [03] CMSeeK")
        print("    [04] Sublist3r")
        print("\n    [00] Back\n")
        ch = input("Choose Tool > ")
        if ch in ["1", "01"]: websploit()
        elif ch in ["2", "02"]: xattacker()
        elif ch in ["3", "03"]: cmseek()
        elif ch in ["4", "04"]: sublist3r()
        else: restart_program()

    # Database Assessment
    elif rm.strip() in ["4", "04"]:
        clear()
        print("\n[ DATABASE ASSESSMENT TOOLS ]\n")
        print("    [01] DbDat")
        print("    [02] NoSQLMap")
        print("    [03] sqlmap")
        print("\n    [00] Back\n")
        ch = input("Choose Tool > ")
        if ch in ["1", "01"]: dbdat()
        elif ch in ["2", "02"]: nosqlmap()
        elif ch in ["3", "03"]: sqlmap()
        else: restart_program()

    # Update / Exit
    elif rm.strip() in ["5", "05"]:
        print("[*] Updating TEAM S-H-T...")
        timeout(2)
        os.system("git pull")
        restart_program()
    elif rm.strip() in ["0", "00"]:
        print("\n[*] Exiting TEAM S-H-T..."); timeout(1); sys.exit()
    else:
        print("\nERROR: Wrong Input"); timeout(1); restart_program()

if __name__ == "__main__":
    main()