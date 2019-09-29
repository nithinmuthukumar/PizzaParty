from math import *

# CONSTANTS
toppings = [line.strip() for line in open("data/toppings.txt").readlines()]


class Person:
    def __init__(self, is_veg, toppings):
        self.is_veg = is_veg
        self.toppings = toppings
        
#DOES NOT VERIFY MEAT VS VEGETARIAN
def optimize_pizzas_A(people,slices):
    round_pizza_slices = 0
    build_pizza_slices = 0
    #deep_dish_slices = 0
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
            
    pizza_set = []
    pizza_set2 = []
    pizza_loose = []
    for i in veg_num:
        if i*slices % 8 == 0 and i*slices >= 8:
            indx = veg_num.index(i)
            for i in range(int(i*slices/8)):
                pizza_set.append([veg_pizzas[indx],veg_pizzas[indx]])
            del veg_num[indx]
            del veg_pizzas[indx]
            
        elif i*slices > 8:
            add_num = floor(i*slices/8)
            indx = veg_num.index(i)
            for i in range(add_num):
                pizza_set.append([veg_pizzas[indx],veg_pizzas[indx]])
            veg_num[indx] -= add_num*8
    for i in veg_num:
        if i*veg_num == 4:
            if len(pizza_set) > 0:
                indx = veg_num.index(i)
                if len(pizza_set[-1]) == 1:
                    pizza_set[-1].append(veg_pizzas[indx])
                else:
                    pizza_set.append([veg_pizzas[indx]])
    if len(veg_pizzas) > 0:
        if len(veg_pizzas[-1]) == 2:
            veg_pizzas[-1].append(veg_pizzas[-1][0])
    for i in range(len(veg_num)):
        lst = veg_pizzas[i]
        lst.append(veg_num[i]*slices)
        pizza_loose.append(lst)



    for i in meat_num:
        if i*slices % 8 == 0 and i*slices >= 8:
            indx = meat_num.index(i)
            for i in range(int(i*slices/8)):
                pizza_set2.append([meat_pizzas[indx],meat_pizzas[indx]])
            del meat_num[indx]
            del meat_pizzas[indx]
            
        elif i*slices > 8:
            add_num = floor(i*slices/8)
            indx = meat_num.index(i)
            for i in range(add_num):
                pizza_set2.append([meat_pizzas[indx],meat_pizzas[indx]])
            meat_num[indx] -= add_num*8
    for i in meat_num:
        if i*meat_num == 4:
            if len(pizza_set2) > 0:
                indx = meat_num.index(i)
                if len(pizza_set2[-1]) == 1:
                    pizza_set2[-1].append(meat_pizzas[indx])
                else:
                    pizza_set2.append([meat_pizzas[indx]])
    if len(meat_pizzas) > 0:
        if len(meat_pizzas[-1]) == 2:
            meat_pizzas[-1].append(meat_pizzas[-1][0])
    for i in range(len(meat_num)):
        lst = meat_pizzas[i]
        lst.append(meat_num[i]*slices)
        pizza_loose.append(lst)

    return [pizza_set,pizza_set2,pizza_loose]


x = Person(True,["olives"])
y = Person(True,["olives"])
z = Person(False,["pepperoni"])
a = Person(False,["pepperoni"])
b = Person(False,["pepperoni","olives"])
lst = [x,y,z,a,b]


#add slice number
#compress down to 2d array


print(optimize_pizzas_A(lst,4))
