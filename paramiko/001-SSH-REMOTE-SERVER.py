#!/usr/bin/python3.10
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.126',username='admin',password='admin@123',port=22)
#stdin, stdout,stderr = ssh.exec_command('whami')
#stdin, stdout, stderr = ssh.exec_command('whoami')
#stdin, stdout, stderr = ssh.exec_command('uptime')
stdin, stdout, stderr = ssh.exec_command('free -m')

print("=====================")
print("The output is: ")
print(stdout.read())

print("The error is: ")
print(stderr.read())

print("=====================")
print("The output is: ")
print(stdout.readlines())


print("The error is: ")
print(stderr.readlines())
