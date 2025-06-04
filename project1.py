# project with dictionary and condiional system
# cafe management system

#menu of restaurat
menu={
    'Pizza': 40,
    'Pasta': 70,
    'salad': 70,
    'Burger': 60,
    'coffee': 80,
}

#greet
print("Welcome to Python restaurant")
print("Pizza: Rs40\nPasta: Rs50\nBurger: Rs60\nCoffee: 80\nSalad: 70")

order_total=0
item1= input("Enter the name of item you want to order=")
if item1 in menu:
    order_total+=menu[item1]
    print(f"Your item{item1} has been added to your order")

else:
    print(f"Please order something else, {item1} is not currently available")

another_order=input("do you want something else? Yes/No")
if another_order=="yes":
    item2=input("enter the name of second item=")
    if item2 in menu:
        order_total+=menu[item2]
        print(f"item {item2} has been added")
    else:
        print(f"order item{item2} is not available!")

print(f"the total amount of your item is{order_total}")