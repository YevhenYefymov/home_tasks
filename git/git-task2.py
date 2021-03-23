#! /usr/bin/python3

import os
import argparse

#init arg parser
parser = argparse.ArgumentParser()
parser.add_argument('--name', help='name of the repository to be edited', required=True)
args = parser.parse_args()

name = args.name
os.chdir("./{}".format(name))

def showLog():
    os.system("git log -10 --oneline")
    
def showDiff():
    print(">>>>>> show diff of latest commit")
    os.system("git log -p -1")

def revertCommits():
    print(">>>>>> revert last 2 commits")
    os.system("git revert --no-commit HEAD")
    os.system("git revert --no-commit HEAD~")
    os.system('git commit -m "revert last 2 commits"')
    
    print(">>>>>> show git log")
    showLog()
    
    showDiff()

def resetCommits():
    # mixed
    print(">>>>>>> perform mixed reset")
    os.system("git reset HEAD~")
    
    print(">>>>>>> show git status")
    os.system("git status")
    
    print(">>>>>>> drop the changes")
    os.system("git checkout .")
    
    print(">>>>>>> show git log")
    showLog()

    # soft
    print(">>>>>>> perform soft reset")
    os.system("git reset --soft HEAD~")
    print(">>>>>>>show git status")
    os.system("git status")
    
    print(">>>>>>> drop the changes")
    os.system("git reset .")
    os.system("git checkout .")
    
    print(">>>>>>> show git log")
    showLog()

    #hard
    print(">>>>>>> perform hard reset")
    os.system("git reset --hard HEAD~")
    print(">>>>>>> show git log")
    showLog()

def getAllTxt():
    files = os.listdir("./")
    result = []
    for file in files:
        if file.endswith(".txt"):
            result.append(file)
    return result

def addTxtToGitignore():
    print(">>>>>>> add all txt files to .gitignore")
    files = getAllTxt()
    with open("./.gitignore", "w") as f:
        for file in files:
            f.write(file + '\n')
    
    os.system("git add .gitignore")
    os.system('git commit -m "update .gitignore" ')

def addFilesToLastCommit():
    os.system("git reset HEAD~")
    os.system("touch fileToAdd1 fileToAdd2")
    os.system("git add .")
    os.system('git commit -m "adding two files to the last commit" ')

def moveUntrackedFiles():
    print(">>>>>>> move untracked files to ./untracked files")
    os.system('git ls-files --other --exclude "*tracked*" | xargs -i mv {} ./untracked_files')

def moveTrackedFiles():
    print(">>>>>>> move tracked files to ./tracked files")
    os.system('git ls-files | xargs -i mv {} ./tracked_files')
    
def lsFilesAndCommit():
    moveUntrackedFiles()
    moveTrackedFiles()
        
    os.system("git add *tracked*")
    os.system("git checkout .")
    os.system('git commit -m "write ls-files" ')

    
revertCommits()
resetCommits()
addTxtToGitignore()
lsFilesAndCommit()
