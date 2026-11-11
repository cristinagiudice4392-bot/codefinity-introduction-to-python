grocery_inventory={"Milk":("Dairy",3.50,8),
                  "Eggs":("Dairy",5.50,8),
                  "Bread":("Bakery",2.99,15),
                  "Apples":("Produce",1.50,50)}
#Task 2
if grocery_inventory["Eggs"][1]>5:
    print("Eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"]=(grocery_inventory["Eggs"][0],
                               grocery_inventory["Eggs"][1]-1,
                               grocery_inventory["Eggs"][2])
else: 
    print("The price of Eggs is reasonable.")
#Task 3
grocery_inventory["Tomatoes"]=("Produce",1.20,30)
print("Inventory after adding Tomatoes: ",grocery_inventory)
#Task 4
milk_stock=grocery_inventory["Milk"][2]
if milk_stock<10:
    milk_stock=milk_stock+20
    grocery_inventory["Milk"]=(grocery_inventory["Milk"][0],
                              grocery_inventory["Milk"][1],
                              milk_stock)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
#Task 5
if grocery_inventory["Apples"][1]>2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")
else: grocery_inventory
#Task 6
print("Updated inventory: ",grocery_inventory)