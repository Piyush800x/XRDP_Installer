#!/bin/bash

figlet XPRD INSTALLER PART 2
sudo dnf install xrdp -y
sudo systemctl start xrdp
sudo systemctl enable xrdp
sudo systemctl start firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --permanent --add-port=3389/tcp
sudo firewall-cmd --reload
sudo chcon --type=bin_t /usr/sbin/xrdp
sudo chcon --type=bin_t /usr/sbin/xrdp-sesman