import config
import pymongo
import Optimization
from pprint import *

class Party:

    client = pymongo.MongoClient(config.CONNECTION_STRING)
    parties_collect = client["userdata"]["parties"]

    '''
    def __init__(self):
        # init stuff
        #self.accounts_collect = self.client["userdata"]["accounts"]
        pass
    '''
    '''
    #approves or denies auth
    def auth(self,username,password):
        if self.accounts_collect.find_one({"username":username,"password":password}) != None:
            return True
        return False
    '''

    #maybe just make all of these static methods
    @staticmethod
    def create_new_party(new_party_name,pizza_list):
        Party.parties_collect.insert_one({"party_name":new_party_name,"members":[],"pizza_prefabs":[],"pizzas":[]})
        for prefab in pizza_list:
            Party.add_pizza_prefab(prefab)

    @staticmethod
    def delete_party(party_name):
        Party.parties_collect.delete_one({"party_name":party_name})

    @staticmethod
    def add_member(party_name,new_member):
        #member comes in the form {"name::name,"toppings":[]}
        Party.parties_collect.find_one_and_update({"party_name":party_name},{"$push":{"members":new_member}},upsert=False)

    @staticmethod
    def remove_member(party_name,target_member):
        Party.parties_collect.find_one_and_update({"party_name":party_name},{"$pull":{"members":target_member}})

    @staticmethod
    def get_member_list(party_name):
        return Party.parties_collect.find_one({"party_name":party_name})["members"]

    '''
    @staticmethod
    def create_new_pizza(party_name,pizza_id): #creates new pizza if name does not exist
        new_pizza = {"pizza_id":pizza_id,"toppings":[],"slices":8}
        Party.parties_collect.find_one_and_update({"party_name":party_name},{"$push":{"pizzas":new_pizza}},upsert=False)
    '''

    @staticmethod
    def create_new_pizza(party_name,pizza_data):
        Party.parties_collect.find_one_and_update({"party_name":party_name},{"$push":{"pizzas":pizza_data}},upsert=False)

    @staticmethod
    def get_pizza_list(party_name):
        return Party.parties_collect.find_one({"party_name":party_name})["pizzas"]

    @staticmethod
    def add_topping(party_name,pizza_id,topping):
        Party.parties_collect.find_one_and_update({"party_name":party_name,"pizzas.pizza_id":pizza_id},{"$push":{"pizzas.$.toppings":topping}},upsert=False)

    @staticmethod
    def remove_topping(party_name,pizza_id,topping):
        Party.parties_collect.find_one_and_update({"party_name":party_name,"pizzas.pizza_id":pizza_id},{"$pull":{"pizzas.$.toppings":topping}})

    @staticmethod
    def compute_optimal_pizza(party_name):
        peoples = []
        for p in Party.parties_collect["members"]:
            person = Optimization.Person(p["toppings"])

        Optimization.optimize_pizzas_A(peoples,2) #hardcoded for two slices


    #host pizza stuff
    @staticmethod
    def add_pizza_prefab(party_name,pizza_prefab):
        Party.parties_collect.find_one_and_update({"party_name": party_name}, {"$push": {"pizza_prefabs": pizza_prefab}},upsert=False)

    @staticmethod
    def remove_pizza_prefab(party_name,prefab_id):
        Party.parties_collect.find_one_and_update({"party_name": party_name}, {"$pull": {"prefab_id": prefab_id}})

    @staticmethod
    def get_pizza_prefab_list(party_name):
        return Party.parties_collect.find_one({"party_name": party_name})["pizza_prefabs"]

    @staticmethod
    def add_user_pizza(party_name,topping):
        pass


#pprint(accounts)
db = Party()
#print(db.auth("daniel_loo","yeetusmeetus"))

#db.create_new_party("daniel's better party")
#pizza_prefab = {"prefab_id":"lmao prefab","toppings":["fungus"]}
#db.add_pizza_prefab("daniel's better party",pizza_prefab)
db.remove_pizza_prefab("daniel's better party","lmao prefab")
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
