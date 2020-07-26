# Nagios Setup Using Ansible
ansible_nagios_setup
This repository is for creating aws ec2 instances and installing and configuring Nagios Core and NRPE(on client) using Ansible.

# Prerequisites
The following permissions are required for the user/tester:
1. Git and Ansible to be installed in local.
2. EC2 full access.
3. AWSCLI security credentials. 
4. A security group with SSH, HTTP and HTTPS access (basic setup).
5. A keypair. Preferably stored in .ssh/ directory in local.

With the help of these Ansible Scripts, you can:

1. Launch 2 EC2 instances with name nagios_core and nagios_client
2. Install and Configure Nagios Client
3. Install and Configure Nagios Core

# Instructions:

1. Before running the playbook , the following things have to be installed and configured in your local machine. 
   
* GIT
* AWSCLI configured with credentials of the IAM user
* Ansible
   
2. Before launching the EC2 instance, make sure that the /vars/main.yml has been configured. You can edit the variables which will determine the launch configuration of the EC2 instance.You can change the values of the following:
   
* Keypair name
* Region
* Instance Type
* AMI
* Count
* Subnet ID
* Security group ID
* SSH Path (Path where the keypair exists on your local machine)

3. GitLab recovery is only possible if the installed version matches the version of the GitLab backup. We can choose the version of GitLab-CE that has to be installed by editing /gitlab/roles/ansible-role-gitlab/defaults/main.yml file.

4. Run execute.sh ->  ./execute.sh

5. You will get a prompt to enter the IAM credentials i.e access-key and secret-key. 
6. Once the playbook is completed. Go to browser ->  <nagios_core_IP>/nagios 
7. Use default nagios credentials.
