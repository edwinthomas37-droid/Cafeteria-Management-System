def bill(order, menu):

    subtotal = 0

    print("\n========== BILL ==========")

    for item, quantity in order.items():

        name, price = menu[item]

        amount = price * quantity
        subtotal += amount

        print(name, "x", quantity, "=", "₹", amount)

    gst = subtotal * 0.05
    total = subtotal + gst

    print("--------------------------")
    print("Subtotal :", "₹", subtotal)
    print("GST 5%   :", "₹", gst)
    print("Total    :", "₹", total)

    return total