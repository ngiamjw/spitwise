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
    values = load_value(filename)
    print(type(values))
    values = ast.literal_eval(values)
    print(type(values))
    print(values)
except:
    values = {}

while True:
    user_input = input()
    values[user_input] = input("?")
    save_value(str(values), filename)
    print(values)