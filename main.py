menu = {
    'Pizza' : 90,
    'Pasta' : 40,
    'Tea' : 30,
    'Coffee' : 80,
    'Burger' : 70,
    'Salad' : 60,
}

print("Hello, Welcome to our Restaurant...!")

print(f"'Pizza' : Rs 90 /-\n'Pasta' : Rs 40 /-\n'Tea' : Rs 30 /-\n'Coffee' : Rs 80 /-\n'Burger' : Rs 70 /-\n'Salad' : Rs 60 /-")

order_total = 0


item_1 = input("Enter the name of the item you want to order : ")

if item_1 in menu : 
    order_total += menu[item_1]
    print(f"Your item, {item_1} has been added to your order...")
else :
    print(f"This item, {item_1} is not available now...\nSorry...!")

another_order = input("Do you want to order something else...?(Yes/No) : ")

if another_order.lower() == "yes":
    while True :
        item_1 = input("Enter the name of the item you want to order : ")

        if item_1 in menu : 
            order_total += menu[item_1]
            print(f"Your item, {item_1} has been added to your order...")
        else :
            print(f"This item, {item_1} is not available now...\nSorry...!")

        another_order = input("Do you want to order something else...?(Yes/No) : ")

        if another_order.lower() == "no" :
            break

print(f"Total Ammount to be pay Rs {order_total} /-")