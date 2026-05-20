inventory = {}

while True:
    print("\n===== INVENTORY MANAGER =====")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        product = input("Product name: ")
        quantity = int(input("Quantity: "))

        inventory[product] = quantity

        print(f"{product} added successfully!")

    elif option == "2":
        print("\n===== INVENTORY =====")

        if len(inventory) == 0:
            print("Inventory is empty.")

        else:
            for product, quantity in inventory.items():
                print(f"{product}: {quantity}")

    elif option == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid option.")
      
