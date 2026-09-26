customers = []


def customer(name, phone, bill):

    customer = {
        "name": name,
        "phone": phone,
        "bill": bill
    }

    customers.append(customer)

    print("\nCustomer added successfully!")


def show_customers():

    print("\n====== CUSTOMER RECORDS ======")

    if len(customers) == 0:
        print("No records found.")
        return

    for customer in customers:

        print("Name :", customer["name"])
        print("Phone:", customer["phone"])
        print("Bill :", "₹", customer["bill"])
        print("------------------------------")