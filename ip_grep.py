#!/bin/python
from sys import argv
import os
import subprocess

script, region = argv
ec2_region_string = ""
ec2_region_string = ec2_region_string.join(region)

coreIP = subprocess.check_output("aws --region "+ec2_region_string+" ec2 describe-instances --filters Name=tag:Name,Values=nagios_core --query 'Reservations[*].Instances[*].[PrivateIpAddress]' --output text", shell=True, stderr=subprocess.STDOUT).rstrip('\n')
clientIP = subprocess.check_output("aws --region "+ec2_region_string+" ec2 describe-instances --filters Name=tag:Name,Values=nagios_client --query 'Reservations[*].Instances[*].[PrivateIpAddress]' --output text", shell=True, stderr=subprocess.STDOUT).rstrip('\n')

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

assign_host = "       ansible_ssh_private_key_file={}    ansible_ssh_user=ec2-user".format(string_ssh_path)

os.system("echo [nagios_core] >> hosts")
final_core = coreIP+assign_host
os.system("echo   {} >> hosts".format(final_core))

os.system("echo [nagios_client] >> hosts")
final_client = clientIP+assign_host
os.system("echo   {} >> hosts".format(final_client))

with open("roles/nagios_core_setup/vars/main.yml", "a+") as file_object:
            start = '---\n'
            file_object.write(start)

            file_object.seek(0)
            data = file_object.read(80)
            if len(data) > 0 :
                b = ' nagios-client-ip: "{}"'.format(clientIP)
                file_object.write(b)
            file_object.close()
