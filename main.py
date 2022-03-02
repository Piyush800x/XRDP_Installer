import os
import time
import sys

os.system("sudo yum install nano -y")
os.system("sudo yum install firewalld -y")
os.system("sudo yum install figlet -y")


def user():
    ans = input("Do you have a non-root user (Y/N): ").upper()

    if ans == "N":
        print("You need to create a non-root user")
        print("Creating a non-root user...")
        user = input("Enter the username: ")
        os.system("sudo adduser {}".format(user))
        os.system("sudo passwd {}".format(user))
        print("User Creation Done")
    elif ans == "Y":
        print("You don't need to worry")
    else:
        print("invalid Option")
        return ans


def env():
    ans2 = input("Select a desktop environment(Enter the number): ")

    if ans2 == "1":
        print("Installing Cinnamon Desktop Environment")
        os.system("sudo dnf install @cinnamon-desktop-environment -y")
    elif ans2 == "2":
        print("Installing Deepin Desktop")
        os.system("sudo dnf install @deepin-desktop-environment -y")
    elif ans2 == "3":
        print("Installing KDE Plasma Desktop Environment")
        os.system("sudo dnf install @kde-desktop-environment -y")
    elif ans2 == "4":
        print("installing XFCE Desktop")
        os.system("sudo dnf install @xfce-desktop-environment -y")
    else:
        print("Invalid Option Try Again")
        return ans2


while True:
    os.system("figlet XRDP INSTALLER PART 1")
    user()
    os.system("sudo dnf upgrade -y")
    os.system("sudo dnf grouplist -v")
    print("--------------------------------------")
    print("1. Cinnamon Desktop Environment")
    print("2. Deepin Desktop")
    print("3. KDE Plasma Desktop Environment")
    print("4. XFCE Desktop")
    print("--------------------------------------")
    env()
    print("Desktop Environment Installation Complete")
    print("Rebooting in 10 seconds...")
    time.sleep(10)
    os.system("sudo reboot")
