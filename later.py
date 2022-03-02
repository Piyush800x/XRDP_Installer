import os

os.system("figlet XPRD INSTALLER PART 2")
os.system("sudo dnf install xrdp -y")
os.system("sudo systemctl start xrdp")
os.system("sudo systemctl enable xrdp")
os.system("sudo systemctl start firewalld")
os.system("sudo systemctl enable firewalld")

os.system("sudo firewall-cmd --permanent --add-port=3389/tcp")
os.system("sudo firewall-cmd --reload")

os.system("sudo chcon --type=bin_t /usr/sbin/xrdp")
os.system("sudo chcon --type=bin_t /usr/sbin/xrdp-sesman")
