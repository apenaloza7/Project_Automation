import sys
import os
from github import Github

path = "/Users/Alex/Documents/Projects/Project_Automation/"

username = "apenaloza7" #Insert your github username here
password = "Iamthecoolest336" #Insert your github password here

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(username, password).get_user()
    repo = user.create_repo(sys.argv[1])
    print("Succesfully created repository {}".format(sys.argv[1]))

create()
