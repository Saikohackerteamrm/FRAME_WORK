 #!/usr/bin/env python3
# TEAM S-H-T Hacking Framework (Full Version)
# Author: TEAM S-H-T #RM Rony Ali (Saiko)

import os, sys
from time import sleep as timeout

# ---------- BASIC SYSTEM FUNCTION ----------
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
    os.chdir(name)

# ---------- TOOL FUNCTIONS (AUTO INSTALL + RUN) ----------

# ---- Information Gathering ----
def nmap():
    install("nmap")
    target = input("[?] Target IP or Domain: ")
    os.system(f"nmap -sV {target}")
    timeout(2)

def red_hawk():
    install("php")
    clone_tool("https://github.com/Tuhinshubhra/RED_HAWK.git")
    os.system("php rhawk.php")

def dtect():
    clone_tool("https://github.com/shawarkhanethicalhacker/D-TECT-1.git")
    os.system("python2 d-tect.py")

def sqlmap():
    install("python")
    clone_tool("https://github.com/sqlmapproject/sqlmap.git")
    os.system("python sqlmap.py --wizard")

def reconDog():
    clone_tool("https://github.com/s0md3v/ReconDog.git")
    os.system("python dog")

# ---- Vulnerability Analysis ----
def routersploit():
    install("python")
    clone_tool("https://github.com/threat9/routersploit.git")
    os.system("python rsf.py")

def androbugs():
    install("python")
    clone_tool("https://github.com/AndroBugs/AndroBugs_Framework.git")
    os.system("python androbugs.py -h")

def wpscan():
    install("ruby")
    os.system("gem install wpscan")
    target = input("[?] Target Website: ")
    os.system(f"wpscan --url {target}")

def sn1per():
    clone_tool("https://github.com/1N3/Sn1per.git")
    os.system("./sniper")

# ---- Web Hacking ----
def websploit():
    clone_tool("https://github.com/websploit/websploit.git")
    os.system("python websploit.py")

def xattacker():
    clone_tool("https://github.com/Moham3dRiahi/XAttacker.git")
    os.system("perl XAttacker.pl")

def cmseek():
    clone_tool("https://github.com/Tuhinshubhra/CMSeeK.git")
    os.system("python cmseek.py")

def sublist3r():
    clone_tool("https://github.com/aboul3la/Sublist3r.git")
    os.system("python sublist3r.py -h")

# ---- Database Assessment ----
def dbdat():
    clone_tool("https://github.com/foospidy/DbDat.git")
    os.system("python DbDat.py")

def nosqlmap():
    clone_tool("https://github.com/codingo/NoSQLMap.git")
    os.system("python nosqlmap.py")

# ---------- MAIN MENU ----------
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
    print("\033[32m   [02] Vulnerability Analysis")
    print("\033[32m   [03] Web Hacking")
    print("\033[32m   [04] Database Assessment")
    print("\033[32m   [05] Update By TEAM S-H-T\n")
    print("\033[31m   [00] Exit TEAM S-H-T\n")
    rm = input("\033[93mSaiko > Fuck_You:- ")

    # ----------- INFORMATION GATHERING -----------
    if rm.strip() == "1" or rm.strip() == "01":
        clear()
        print("\n[ INFORMATION GATHERING TOOLS ]\n")
        print("    [01] Nmap")
        print("    [02] Red Hawk")
        print("    [03] D-TECT")
        print("    [04] sqlmap")
        print("    [05] ReconDog")
        print("\n    [00] Back to main menu\n")
        infogathering = input("Saiko > Fuck_You ")
        if infogathering == "1" or infogathering == "01": nmap()
        elif infogathering == "2" or infogathering == "02": red_hawk()
        elif infogathering == "3" or infogathering == "03": dtect()
        elif infogathering == "4" or infogathering == "04": sqlmap()
        elif infogathering == "5" or infogathering == "05": reconDog()
        elif infogathering == "0" or infogathering == "00": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1);restart_program()

    # ----------- VULNERABILITY ANALYSIS -----------
    elif rm.strip() == "2" or rm.strip() == "02":
        clear()
        print("\n[ VULNERABILITY ANALYSIS TOOLS ]\n")
        print("    [01] Routersploit")
        print("    [02] AndroBugs Framework")
        print("    [03] WPScan")
        print("    [04] Sn1per")
        print("\n    [00] Back to main menu\n")
        vulnsys = input("Saiko > Fuck_You ")
        if vulnsys == "1" or vulnsys == "01": routersploit()
        elif vulnsys == "2" or vulnsys == "02": androbugs()
        elif vulnsys == "3" or vulnsys == "03": wpscan()
        elif vulnsys == "4" or vulnsys == "04": sn1per()
        elif vulnsys == "0" or vulnsys == "00": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1);restart_program()

    # ----------- WEB HACKING -----------
    elif rm.strip() == "3" or rm.strip() == "03":
        clear()
        print("\n[ WEB HACKING TOOLS ]\n")
        print("    [01] Websploit")
        print("    [02] XAttacker")
        print("    [03] CMSeeK")
        print("    [04] Sublist3r")
        print("\n    [00] Back to main menu\n")
        webhack = input("Saiko > Fuck_You ")
        if webhack == "1" or webhack == "01": websploit()
        elif webhack == "2" or webhack == "02": xattacker()
        elif webhack == "3" or webhack == "03": cmseek()
        elif webhack == "4" or webhack == "04": sublist3r()
        elif webhack == "0" or webhack == "00": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1);restart_program()

    # ----------- DATABASE ASSESSMENT -----------
    elif rm.strip() == "4" or rm.strip() == "04":
        clear()
        print("\n[ DATABASE ASSESSMENT TOOLS ]\n")
        print("    [01] DbDat")
        print("    [02] NoSQLMap")
        print("    [03] sqlmap")
        print("\n    [00] Back to main menu\n")
        dbssm = input("Saiko > Fuck_You ")
        if dbssm == "1" or dbssm == "01": dbdat()
        elif dbssm == "2" or dbssm == "02": nosqlmap()
        elif dbssm == "3" or dbssm == "03": sqlmap()
        elif dbssm == "0" or dbssm == "00": restart_program()
        else: print("\nERROR: Wrong Input");timeout(1);restart_program()

    # ----------- UPDATE & EXIT -----------
    elif rm.strip() == "05":
        print("[*] Updating TEAM S-H-T..."); timeout(2)
        os.system("git pull")
        restart_program()
    elif rm.strip() == "0" or rm.strip() == "00":
        print("\n[*] Exiting TEAM S-H-T..."); timeout(1); sys.exit()
    else:
        print("\nERROR: Wrong Input"); timeout(1); restart_program()

if __name__ == "__main__":
    main()