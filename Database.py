import config
import pymongo
from pprint import *

class Database:

    def __init__(self):
        # init stuff
        self.client = pymongo.MongoClient(config.CONNECTION_STRING)
        self.accounts_collect = self.client["userdata"]["accounts"]
        self.parties_collect = self.client["userdata"]["parties"]

    #approves or denies auth
    def auth(self,username,password):
        if self.accounts_collect.find_one({"username":username,"password":password}) != None:
            return True
        return False

    def create_new_party(self,new_party_name):
        self.parties_collect.insert_one({"party_name":new_party_name,"members":[],"pizzas":[]})

    def delete_party(self,party_name):
        self.parties_collect.delete_one({"party_name":party_name})
        
    def add_member(self,party_name,new_member):
        self.parties_collect.find_one_and_update({"party_name":party_name},{"$push":{"members":new_member}},upsert=False)

    def remove_member(self,party_name,target_member):
        self.parties_collect.find_one_and_update({"party_name":party_name},{"$pull":{"members":target_member}})

    def get_member_list(self,party_name):
        return self.parties_collect.find_one({"party_name":party_name})["members"]

    def create_new_pizza(self,party_name,pizza_id): #creates new pizza if name does not exist
        new_pizza = {"pizza_id":pizza_id,"toppings":[]}
        self.parties_collect.find_one_and_update({"party_name":party_name},{"$push":{"pizzas":new_pizza}},upsert=False)

    def add_topping(self,party_name,pizza_id,topping):
        self.parties_collect.find_one_and_update({"party_name":party_name,"pizzas.pizza_id":pizza_id},{"$push":{"pizzas.$.toppings":topping}},upsert=False)

    def remove_topping(self,party_name,pizza_id,topping):
        self.parties_collect.find_one_and_update({"party_name":party_name,"pizzas.pizza_id":pizza_id},{"$pull":{"pizzas.$.toppings":topping}})

#pprint(accounts)
db = Database()
#print(db.auth("daniel_loo","yeetusmeetus"))

#db.create_new_party("daniel's better party")
'''
n_party = db.get_party_json("nithin's party")
n_party["members"].append("danielle")
print(n_party)
'''

#db.add_member("nithin's party","nitihn")
#db.remove_member("nithin's party","nitihn")
#print(db.get_member_list("nithin's party"))
#db.delete_party("daniel's better party")
#db.create_new_pizza("nithi's trash party","bad pizza")
#print(db.remove_topping("daniel's better party","moi pizza","shrooms"))

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
