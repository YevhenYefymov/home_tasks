#! /usr/bin/python3

import argparse
import os

#init arg parser
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='name of the repository to be created', required=True)
args = parser.parse_args()

# name of the repository; it's directory is the same as the name
name = args.name

# define functions
def initRepo():
    os.mkdir("./{}".format(name))
    os.chdir("./{}".format(name))
    os.system("git init ./")

def setupCredentials():
    os.system("ls")
    userName = input("Please enter git user name\n")
    os.system("git config user.name {}".format(userName))
    userEmail = input("Please enter git user email\n")
    os.system("git config user.email {}".format(userEmail))
    print("Credentials are set! Execute git config --list to see the changes")

def createFiles():
    os.system("touch my_file text1.txt text2.txt .gitignore")
    os.system("mkdir untracked_files tracked_files")

def addStringToFile(str=None):
    if not str:
        str = input("Please enter a string to add to my_file\n")
    with open("my_file", "a") as f:
        f.write(str + '\n')

def commit(message):
    os.system("git add my_file")
    os.system('git commit -m "{}"'.format(message))

# run sequence
initRepo()
#setupCredentials()

createFiles()

charsToCommit = "12345"

for char in charsToCommit:
    addStringToFile(char)
    commit("add char {}".format(char))
