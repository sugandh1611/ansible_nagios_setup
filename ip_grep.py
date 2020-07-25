#!/bin/python
import os

os.system("aws ec2 describe-instances --filters  'Name=tag:Name,Values=nagios_core' | grep PrivateIpAddress | grep -o -P '\d+\.\d+\.\d+\.\d+' | grep -v '^10\.' | sort -u > coreIP.txt")
os.system("aws ec2 describe-instances --filters  'Name=tag:Name,Values=nagios_client' | grep PrivateIpAddress | grep -o -P '\d+\.\d+\.\d+\.\d+' | grep -v '^10\.' | sort -u > clientIP.txt")

f_ssh=open("vars/main.yml","r")

string_ssh=""
for line in f_ssh:
    string_ssh=string_ssh+line
string_ssh=string_ssh.strip()
string_ssh=string_ssh.rstrip()
string_ssh=string_ssh.replace(" ","")

string_ssh_path_pos=string_ssh.find("sshpath")
string_ssh_path=string_ssh[string_ssh_path_pos+9:]
end_pos=string_ssh_path.find("\"")

string_ssh_path=string_ssh_path[:end_pos]

f_ssh.close()


f1=open("coreIP.txt","r")

assign_host_core="       ansible_ssh_private_key_file="+string_ssh_path+"    ansible_ssh_user=ec2-user"
rd1=f1.read().splitlines()
os.system("echo [nagios_core] >> hosts")
x1=len(rd1)
final=rd1[0]+assign_host_core
os.system("echo   {} >> hosts".format(final))

f1.close()

f2=open("clientIP.txt","r")

assign_host_client="       ansible_ssh_private_key_file="+string_ssh_path+"    ansible_ssh_user=ec2-user"
rd2=f2.read().splitlines()
os.system("echo [nagios_client] >> hosts")
x2=len(rd2)
final=rd2[0]+assign_host_client
os.system("echo   {} >> hosts".format(final))

f2.close()
