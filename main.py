import argparse
from mssql import *
from threading import Thread
import requests
from requests.auth import HTTPBasicAuth
import json

parser=argparse.ArgumentParser()

parser.add_argument("--name", help="all or specific")
parser.add_argument("--date", help="select a date")
parser.add_argument("--venue", help="select a venue")
parser.add_argument("--thread", help="number of threads to execute")
parser.add_argument("--db", help="which database to use")
parser.add_argument("--schedule", help="file for scheduling")

args=parser.parse_args() #Load all the args
tot=0 #initial number of active threads
file_lines = [] #Lines of schedule text file

#connect to database here for the moment it's MS SQL Server
if str(args.db) == "mssql":
    #mssql_prepare()
    pass

#read schedule file
#file = open(str(args.schedule), 'r')
#for line in file.readlines():
#    file_lines.append(line.replace("\n",""))

def thread_function():
    print("started a new job number : "+str(tot))
    _url = "http://saas.derbysapp.com/user-remarks/?rdate=2022-09-18&venue=ST&raceno=1&uid=1&role=admin"
    _username = "pub_0aa31cc8f20ca6ec1ec9d8ec78cd3808"
    _pwd = "pri_aa6792647ccaa40e89217e8119abac82"
    response = requests.get(_url,auth = HTTPBasicAuth(_username, _pwd))
    # Save the response to database 
    if str(args.db) != "mssql":
        m = json.dumps(response.text)
        k = str(m).replace("\"","X69X")
        j = str(k).replace('\\','JJX')
        print(m+"\n")
        print(k+"\n")
        print(j+"\n")
        #mssql_save_data(k)
        #mssql_show_data()
mssql_prepare()
#Start all the threads
for i in range(int(args.thread)):
    tot+=1
    Thread(target=thread_function).start()