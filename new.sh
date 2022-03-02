#!/usr/bin/bash

sudo yum install python -y
sudo yum install nano -y
sudo yum install firewalld -y
sudo yum install figlet -y
sudo yum install wget -y
sleep 5
figlet XRDP INSTALLER
sleep 3
sudo python3 new.py
