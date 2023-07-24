food_list = ["Tandoori Chicken", "Burger", "Pizza", "Sandwitch", "Icecream", "Truffle cake", "Pani puri", "Fried Rice"]
#Admin Functionalites
def admin():
    def edit_food(food):
        food_list.append(food)
    def view():
        return food_list
    def remove(food):
        food_list.pop(food)

# User Functionalites
def greeting():
    print("Welcome to our Foodapp")
    print("Please select any one option from below")
    print("O-New order", "H-Order history", "U-Update profile")
    option = input()
    if option == 'O':
        order_menu()
        
    if option == 'H':
        order_history()

    if option == 'U':
        update()

def order_menu():
    print(food_list)
    food = input("Please select your food:")
    order = []
    if food in food_list: 
        order.append(food)
        print("You want select another item")
        choice = input()
        if choice == 'yes':
            food = input("Please select your food:")
            order.append(food)
        else:
            pass
    print(order)

    
def order_history():
    return order
def update():
    print("Please update your profile")
    Name = input("Enter your Fullname:")
    Phone = input("Enter your phn no:")
    Address = input("Enter your address:")
    Email = input("Enter your Email:")
    password = input("Enter your password:")
    print("Updated successfully")


print("Choose L-login or N-new register")
choice = input()
def login():
    username = input("Enter username:")
    password = input("Enter password:")
    greeting()
def new_register():
    Name = input("Enter your Fullname:")
    Phone = input("Enter your phn no:")
    Address = input("Enter your address:")
    Email = input("Enter your Email:")
    password = input("Enter your password:")
    print("Registration successfully completed, Please login")
    return login()
    greeting()
if choice == "L":
    login()
    
if choice == "N":
    new_register()

print('''Thank you
Visit Again!!..''')

    



    

