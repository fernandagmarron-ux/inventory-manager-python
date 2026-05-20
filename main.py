inventory = {}

while True:
    print("\n===== INVENTORY MANAGER =====")
    print("1. Add product")
    print("2. Show inventory")
    print("3. Delete product")
    print("4. Exit")

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
        product = input("Product to delete: ")

        if product in inventory:
            del inventory[product]
            print(f"{product} deleted successfully!")

        else:
            print("Product not found.")

    elif option == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid option.")
