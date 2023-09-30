#!/usr/bin/python3.10
import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.0.126',username='admin',password='admin@123',port=22)
stdin, stdout, stderr = ssh.exec_command('free')

print(stdout.read())
