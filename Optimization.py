from math import *

# CONSTANTS
toppings = [line.strip() for line in open("toppings.txt").readlines()]
meaties = ["PEPPERONI",
"EXTRA PEPPERONI",
"SAUSAGE",
"BACON",
"BEEF",
"HAM"]

class Person:
    def __init__(self, toppings):
        v2 = False
        self.toppings = toppings
        for t in toppings:
            if meaties.count(t.upper()) > 0:
                self.is_veg = False
                v2 = True
                break
        if not v2:
            self.is_veg = True
            
            #################################################################MCDONALDS COUPON CANADA FOR 2ND BIG MAC FREE IS 320161555
        
                
        
        
#DOES NOT VERIFY MEAT VS VEGETARIAN
def optimize_pizzas_A(people,slices):
    round_pizza_slices = 0
    build_pizza_slices = 0
    veg_pizzas_num = 0
    meat_pizzas_num = 0
    veg_pizzas = []
    meat_pizzas = []
    veg_num = []
    meat_num = []
    for p in people:
        visited = False
        if p.is_veg:
            veg_pizzas_num += slices
            for i in range(len(veg_pizzas)):
                if veg_pizzas[i] == p.toppings:
                    veg_num[i] += 1
                    visited = True
                    break 
            if not visited:
                veg_pizzas.append(p.toppings)
                veg_num.append(1)
        else:
            meat_pizzas_num += slices
            for i in range(len(meat_pizzas)):
                if meat_pizzas[i] == p.toppings:
                    meat_num[i] += 1
                    visited = True
                    break
            if not visited:
                meat_pizzas.append(p.toppings)
                meat_num.append(1)
    
    for i in veg_num:
        x = i % 8
        if x > 4:
            i += 8-x
    for i in meat_num:
        x = i % 8
        if x > 4:
            i += 8-x
    #print(veg_pizzas)
    #print(meat_pizzas)
    pizza_set = []
    deletions = []
    inc = 0
    for i in veg_num:
        if i*slices % 8 == 0 and i*slices >= 8:
            indx = inc
            for i in range(int(i*slices/8)):
                pizza_set.append([veg_pizzas[indx],veg_pizzas[indx],8])
            deletions.append(indx)
            
        elif i*slices > 8:
            add_num = floor(i*slices/8)
            indx = inc
            for i in range(add_num):
                pizza_set.append([veg_pizzas[indx],veg_pizzas[indx],8])
            veg_num[indx] -= add_num*8
        inc += 1
    for i in range(len(deletions)):
        del veg_num[deletions[i]-i]
        del veg_pizzas[deletions[i]-i]
    
    deletions = []
    
    for i in veg_num:
        if i*veg_num == 4:
            if len(pizza_set) > 0:
                indx = veg_num.index(i)
                if len(pizza_set[-1]) == 1:
                    pizza_set[-1].append(veg_pizzas[indx],8)
                else:
                    pizza_set.append([veg_pizzas[indx]])
    
    if len(pizza_set) > 0:
        if len(pizza_set[-1]) == 1:
            pizza_set[-1].append([""])
            pizza_set[-1].append(4)
    
    for i in range(len(veg_num)):
        if len(pizza_set) > 0:
            if pizza_set[-1][1] == ['']:
                pizza_set[-1][1] = [veg_pizzas[i]]
                pizza_set[-1][2] = 8
            else:
                lst = [veg_pizzas[i]]
                lst.append([''])
                if veg_num[i]*slices <= 4:
                    lst.append(4)
                else:
                    lst[1] = lst[0]
                    lst.append(8)
                pizza_set.append(lst)
        else:
            lst = [veg_pizzas[i]]
            lst.append([''])
            if veg_num[i]*slices <= 4:
                lst.append(4)
            else:
                lst[1] = lst[0]
                lst.append(8)
            pizza_set.append(lst)
    


#############################################
    MEATERS = len(pizza_set)
    inc = 0
    for i in meat_num:
        if i*slices % 8 == 0 and i*slices >= 8:
            indx = inc
            for i in range(int(i*slices/8)):
                pizza_set.append([meat_pizzas[indx],meat_pizzas[indx],8])
            deletions.append(indx)
            
            
        elif i*slices > 8:
            add_num = floor(i*slices/8)
            indx = meat_num.index(i)
            for i in range(add_num):
                pizza_set.append([meat_pizzas[indx],meat_pizzas[indx],8])
            meat_num[indx] -= add_num*8
        inc += 1
    for i in range(len(deletions)):
        del meat_num[deletions[i]-i]
        del meat_pizzas[deletions[i]-i]
    
    deletions = []
    
    for i in meat_num:
        if i*meat_num == 4:
            if len(pizza_set) > 0:
                indx = meat_num.index(i)
                if len(pizza_set[-1]) == 1 and len(pizza_set) > MEATERS:
                    pizza_set[-1].append(meat_pizzas[indx])
                else:
                    pizza_set.append([meat_pizzas[indx]])
    
    if len(pizza_set) > 0:
        if len(pizza_set[-1]) == 1:
            pizza_set[-1].append([""])
            pizza_set[-1].append(4)
                    
    for i in range(len(meat_num)):
        print(pizza_set)
        if len(pizza_set) > 0:
            if pizza_set[-1][1] == [''] and len(pizza_set) > MEATERS:
                pizza_set[-1][1] = [meat_pizzas[i]]
                pizza_set[-1][2] = 8
            else:
                lst = [meat_pizzas[i]]
                lst.append([''])
                if meat_num[i]*slices <= 4:
                    lst.append(4)
                else:
                    lst[1] = lst[0]
                    lst.append(8)
                pizza_set.append(lst)
        else:
            lst = [meat_pizzas[i]]
            lst.append([''])
            if meat_num[i]*slices <= 4:
                lst.append(4)
            else:
                lst[1] = lst[0]
                lst.append(8)
            pizza_set.append(lst)
        

    return pizza_set

'''
x = Person(["olives"])
y = Person(["olives"])
z = Person(["pepperoni"])
a = Person(["vegetables,pepperoni"])
b = Person(["pepperoni","olives"])

lst = [x,y,z,a,b]

print(optimize_pizzas_A(lst,4))
'''
