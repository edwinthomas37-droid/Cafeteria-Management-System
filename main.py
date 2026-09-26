from menu import menu, take_order
from billing import bill
from customer import customer, show_customers


while True:

    print("\n==============================")
    print("      CAFE MANAGEMENT")
    print("==============================")

    print("1. New Order")
    print("2. Customer Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("\nEnter customer name: ")
        phone = input("Enter phone number: ")

        order = take_order()

        if order:
            total = bill(order, menu)
            customer(name, phone, total)
        else:
            print("No items ordered.")

    elif choice == "2":

        show_customers()

    elif choice == "3":

        print("Thank you!")
        break

    else:

        print("Invalid choice!")