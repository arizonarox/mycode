#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

def movethemfiles(sftp):
    while True:
        where = input("where do you want to put the files, ie/tmp/ or /home/bender/?")
        try:
            os.path.exists(where) == True
            break
        except:
            print("that path doesn't exist, try again)")
            continue
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            sftp.put("/home/student/filestocopy/"+x, where+x) # move file to target location


## where to connect to
while True: 
    IP = input("What's the ip you want to connect to, ie 10.10.2.3: ")
    
    try:
        t = paramiko.Transport(IP, 22) ## IP and port
    except:
        print("That wasn't a valid ip, try again...")
        continue     
    ## how to connect (see other labs on using id_rsa private/public keypairs)
    U = input("enter the username: ")
    P = input("enter the password: ")
    try:
        t.connect(username=U, password=P)
    except:
        print("your username or password were incorrect, start over...")
        continue
    ## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)
    
    movethemfiles(sftp)

    ## iterate across the files within directory
#    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
#        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
#            sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
    sftp.close() # close the connection
    
    finished = input("Are you done? yes or no: ")
    try:
        if finished == "yes":
            break
        elif finished == "no":
            continue
    except:
        print("you didn't say yes or no... good bye!")
        break
