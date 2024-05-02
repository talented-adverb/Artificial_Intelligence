j1 = int(input("Capacity of jug 1: "))
j2 = int(input("Capacity of jug 2: "))
g = int(input("Amount of water to be measured: "))  # Goal

def display():
    print("\nSelect the rule to be applied")
    print("1: Fill jug 1")
    print("2: Fill jug 2")
    print("3: Empty jug 1")
    print("4: Empty jug 2")
    print("5: Transfer all water from jug 1 to jug 2")
    print("6: Transfer all water from jug 2 to jug 1")
    print("7: Transfer some water from jug 1 to jug 2 until jug 2 is full")
    print("8: Transfer some water from jug 2 to jug 1 until jug 1 is full")

def apply_rule(ch, x, y):
    if ch == 1:
        if g<j1:
            x=g
        return x, y
    elif ch == 2:
        if g<j2:
            y=g        
        return x, y
    elif ch == 3:
        return 0, y
    elif ch == 4:
        return x, 0
    elif ch == 5:
        transfer_amount = min(x, j2 - y)
        return x - transfer_amount, y + transfer_amount
    elif ch == 6:
        transfer_amount = min(y, j1 - x)
        return x + transfer_amount, y - transfer_amount
    elif ch == 7:
        transfer_amount = min(x, j2 - y)
        if (transfer_amount+y)==j2:
            return x - transfer_amount, j2
        else:
            print("Not possible")
            return x,y
    elif ch == 8:
        transfer_amount = min(y, j1 - x)
        if (transfer_amount+x)==j1:
            return j1,y - transfer_amount
        else:
            print("Not possible")
            return x,y 
    else:
        print("Invalid rule number")
        return x, y

# Initialize the capacities of both jugs as 0
x = y = 0

while True:
    if x == g or y == g:
        print('Goal Achieved')
        break
    else:
        display()
        ch = int(input("Enter rule to apply: "))
        x, y = apply_rule(ch, x, y)
        print("\nStatus")
        print("Current state:", x, y)


