menu = {
    1: ("Coffee", 80),
    2: ("Tea", 40),
    3: ("Burger", 120),
    4: ("Pizza", 200),
    5: ("Sandwich", 100),
    6: ("French Fries", 90)
}


def show_menu():
    print("\n========== CAFE MENU ==========")

    for number, item in menu.items():
        print(number, "-", item[0], "₹", item[1])

    print("0 - Finish Order")


def take_order():
    order = {}

    while True:
        show_menu()

        choice = int(input("Enter item number: "))

        if choice == 0:
            break

        if choice not in menu:
            print("Invalid choice!")
            continue

        quantity = int(input("Enter quantity: "))

        order[choice] = order.get(choice, 0) + quantity

        print("Item added!")

    return order