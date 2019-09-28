import math

# CONSTANTS
toppings = [line.strip() for line in open("toppings.txt").readlines()]


class Person:
    def __init__(self, slices, is_veg, pizza_type, pizza_name, toppings, crust, restrictions="none", sides="none", drinks="none"):
        self.slices = slices
        self.is_veg = is_veg
        self.pizza_type = pizza_type
        self.pizza_name = pizza_name
        self.toppings = toppings
        self.crust = crust
        self.restrictions = restrictions
        self.sides = sides
        self.drinks = drinks


def optimize_pizzas_A(people):
    round_pizza_slices = 0
    build_pizza_slices = 0
    deep_dish_slices = 0

    round_pizza_types = {}
    deep_dish_types = {}

    for p in people:
        if p.pizza_type == "ROUND":
            round_pizza_slices += p.slices
            if p.pizza_type not in round_pizza_types:
                round_pizza_slices[p.pizza_type] = p.slices
            else:
                round_pizza_slices[p.pizza_type] += p.slices

        elif p.pizza_type == "BUILD":
            build_pizza_slices += p.slices
        elif p.pizza_type == "DEEP_DISH":
            deep_dish_slices += p.slices
            if p.pizza_type not in deep_dish_slices:
                deep_dish_types[p.pizza_type] = p.slices
            else:
                deep_dish_types[p.pizza_type] += p.slices

    round_pizza_types = sorted(round_pizza_types.items(), key=lambda x: x[1], reverse=True)
    deep_dish_types = sorted(deep_dish_types.items(), key=lambda x: x[1], reverse=True)

    num_pizzas = math.ceil((round_pizza_slices + deep_dish_slices + build_pizza_slices) / 8)

    round_pizzas = [[] for i in range(math.floor(round_pizza_slices / 8))]
    build_pizzas = [[] for i in range(math.floor(build_pizza_slices / 8))]
    deep_dish = [[] for i in range(math.floor(deep_dish_slices / 8))]

    remaining = [len(round_pizzas) * 8 - round_pizza_slices, len(build_pizzas) * 8 - build_pizza_slices,
                 len(deep_dish_types) * 8 - deep_dish_slices]

    tot_remaining = sum(remaining)

    while tot_remaining > 0:
        if remaining.index(max(remaining)) == 0:
            tot_remaining -= 8
            round_pizzas.append([])
            remaining[0] = 0
        elif remaining.index(max(remaining)) == 1:
            tot_remaining -= 8
            build_pizzas.append([])
            remaining[1] = 0
        else:
            tot_remaining -= 8
            build_pizzas.append([])
            remaining[2] = 0

    for i in range(len(round_pizzas)):
        round_pizzas[i] = round_pizza_types[i][0]

    for i in range(len(deep_dish)):
        deep_dish[i] = deep_dish_types[i][0]






