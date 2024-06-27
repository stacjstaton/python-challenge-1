# Menu dictionary
menu = {
    "Appertizers": {
        "Loaded Fries": 5.99,
        "Jalapeno Poppers": 4.99,
        "Pretzel Bites": 3.99,
        "Mozzarella Sticks": 4.99
    },
    "Main Menu": {
        "Philly Cheesesteak": 10.49,
        "Fried Fish": 9.99,
        "Grilled Pork Chops": 8.49,
        "Smoked Sausage": 6.99,
        "Wings": {
            "Lemon Pepper": 8.99,
            "Mango": 10.99,
            "Spicy": 9.99
        },
        "Burger": {
            "Smash": 12.49,
            "Double Cheese Burger": 10.49
        }
    },
    "Drinks": {
        "Smoothee": {
            "Small": 2.99,
            "Medium": 4.49,
            "Large": 5.99
        },
        "Soda": {
            "Sprite": 2.49,
            "Coke": 3.99,
            "Mountain Dew": 2.49
        },
        "Juice": {
            "Orange": 3.99,
            "Pineapple": 4.99,
            "Apple": 3.49
        }
    },
    "Dessert": {
        "Apple Pie": 5.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 5.49
        },
        "Peach Cobbler": 4.99,
        "Blueberry Muffins": 4.99,
        "Chocolate Cake": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
menu_dashes = "-" * 42

# Launch the store and present a greeting to the customer
print("Welcome to the Yummy Good Food Truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("What would you like to order from the menu? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_category = input("Type menu number or q to quit: ")

            # 3. Check if the customer typed a number
            if menu_category.isdigit():
                # Convert the menu selection to an integer
             if int (menu_category) in menu_items.keys():

                # 4. Check if the menu selection is in the menu items

                    # Store the item name as a variable
                    menu_category_name = menu_items[int(menu_category)]

                    # Ask the customer for the quantity of the menu 
                    quantity = input(f"How many of {menu_items} would you like? ")
                    # Check if the quantity is a number, default to 1 if not
                    item_spaces = 1

                    # Add the item name, price, and quantity to the order list
                    print("Item # | Item name                | Price")

                    # Tell the customer that their input isn't valid
                    print(f"{menu_category} was not a valid menu option.")

                    # Tell the customer they didn't select a menu option
                    print(f"{menu_category} Is not a menu option.")
        # Tell the customer they didn't select a number
        print("You did not select a number. Please try again")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        while True:
            print("Which menu option would you like to view? ")

                # Keep ordering
            menu_category = input("Type menu number to view or q to quit: ")

                # Exit the keep ordering question loop
            if menu_category == 'q':


                # Complete the order
                print(f"You selected {menu_category_name}")

                # Since the customer decided to stop ordering, thank them for
                # their order
                print("Thank you for your order of Yummy Good Food Truck menu")

                # Exit the keep ordering question loop
                if menu_category == 'q':


                # Tell the customer to try again
                 print(f"{menu_category} was not a menu option. Please try again.")

# Print out the customer's order
print("This is what we are preparing for you and your order will be completed shortly.\n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
print("Which menu would you like to view? ")
    # 7. Store the dictionary items as variables
menu_category_name = menu_dashes [int(menu_dashes)]

    # 8. Calculate the number of spaces for formatted printing
print(menu_dashes)

    # 9. Create space strings


    # 10. Print the item name, price, and quantity
print("Item # | Item name                | Price")

# 11. Calculate the cost of the order using list comprehension
total_price = sum(item["price"] * item["quantity"] for item in menu_category_name)
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
print(f"The total price of the order is: ${total_price:.2f}")
