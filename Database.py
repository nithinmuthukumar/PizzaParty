import config
import pymongo
from pprint import *

class Database:

     def __init__(self):
          # init stuff
          self.client = pymongo.MongoClient(config.CONNECTION_STRING)


     #approves or denies auth
     def auth(self,username,password):
          accounts_collect = self.client["userdata"]["accounts"]
          if accounts_collect.find_one({"username":username,"password":password}) != None:
               return True
          return False


#pprint(accounts)
db = Database()
print(db.auth("daniel_loo","yeetusmeetus"))



'''
for a in accounts.find():
     print(a)
     

db = client.admin
#get a database
accounts = db.accounts


pprint(accounts)


serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
'''
