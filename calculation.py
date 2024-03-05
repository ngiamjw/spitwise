import names
import ast

filename = "values.txt"

def save_value(input_value, filename):
    with open(filename, 'w') as f:
        f.write(input_value)

def load_value(filename):
    with open(filename, 'r') as f:
        read = f.read()
    return read

try:
    name_dict = ast.literal_eval(load_value(filename))
except:
    name_dict = names.names_sorted()

name_list = list(name_dict.keys())

def unequal_amt(amt, person_paid, temp_dict):
    global name_dict
    not_equal = []
    after_amount = amt
    while True:
        info = input("names")
        info = info.split()
        if input(f"names are {info}, y/n") == 'y':
            not_equal += info
            break
    for name in not_equal:
        amount = int(input(f"amount {name}"))
        after_amount -= amount
        print(f"theres still ${after_amount}")
        temp_dict[person_paid][name] += amount
        temp_dict[name][person_paid] -= amount
    if after_amount != 0:
        print(name_dict)
        unequal_amt(amt, person_paid, name_dict)
    else:
        name_dict = temp_dict

def unequal_percentage(amt, person_paid):
    not_equal = []
    after_amount = 100
    while True:
        info = input("names")
        if info == "":
            break
        not_equal.append(info)
    for name in not_equal:
        amount = int(input(f"% {name}"))
        after_amount -= amount
        print(f"theres still ${after_amount}")
        name_dict[person_paid][name] += amt*(amount/100)
        name_dict[name][person_paid] -= amt*(amount/100)
    if after_amount != 0:
        unequal_percentage(amt, person_paid)

def unequal_amt_gst_and_service(amt, person_paid):
    pass

def equal_amt(amount, person_paid):
    amount = amount/ (len(name_list) - 1)
    for name in name_dict[person_paid]:
        name_dict[person_paid][name] += amount
        name_dict[name][person_paid] -= amount

unequal = {"$": unequal_amt, "%": unequal_percentage, "gst": unequal_amt_gst_and_service}

def get_input():
    person_paid = input(f"who paid? {name_list} ")
    amount = int(input("amount: "))
    equally = input("split equally? yes/no ")

    if equally == "yes":
        equal_amt(amount, person_paid)

    elif equally == "no":
        action = input(f"{list(unequal.keys())}")
        unequal[action](amount, person_paid, name_dict)
        
# def combine():
#     for name in name_dict:
#         total = sum((name_dict[name].values()))
        # if total >= 0:

while True:
    get_input()
    save_value(str(name_dict), filename)
    print(name_dict)
    
        




    

