#Define the menu of Restaurant
menu={
    'Vegbiryani':200,
    'corianderchatni':50,
    'peanutchutni':50,
    'radishchutni':50,
    'tomatochutni':50
}
#print(menu)
print("Welcome to the Cafe Our Menu is: ")
print("Vegbiryani: Rs 200\ncorianderchatni:Rs 50\npeanutchutni:Rs 50\nradishchutni:Rs 50\ntomatochutni:Rs 50")
order_total=0

item_1=input("Enter the name of item you want to order")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order=input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter the name of second item")
    if item_2 in menu:
     order_total+=menu[item_2]
     print(f"Your item {item_2} has been added to your order")
    else:
     print(f"ordered item {item_2} is not available yet")
    
print(f"Your total order amount is Rs: {order_total}")

