# Display welcome message and wood menu
print("Welcome to Maria Eduarda Gonçalves's Lumber Mill!")
print("Please enter the desired wood type:")
print("PIN - Pine Log")
print("PER - Peroba Log")
print("MOG - Mahogany Log")
print("IPE - Ipe Log")
print("IMB - Imbuia Log")


# Function to choose the wood type and return its unit price
def choose_wood_type():
    while True:
        wood_type = input("\nEnter the desired wood type: ").strip().upper()
        if wood_type == "PIN":
            return 150.40
        elif wood_type == "PER":
            return 170.20
        elif wood_type == "MOG":
            return 190.90
        elif wood_type == "IPE":
            return 210.10
        elif wood_type == "IMB":
            return 220.70
        else:
            print("Invalid choice, please enter the wood type again.")
            print("PIN - Pine Log")
            print("PER - Peroba Log")
            print("MOG - Mahogany Log")
            print("IPE - Ipe Log")
            print("IMB - Imbuia Log")


# Function to get log quantity and return quantity + volume discount
def log_quantity():
    while True:
        try:
            qty = int(input("\nEnter the number of logs: "))
            if qty <= 0 or qty > 2000:
                print("We do not accept orders with this number of logs. Please try again.")
                continue
            elif qty < 100:
                return qty, 0.0
            elif 100 <= qty < 500:
                return qty, 0.04
            elif 500 <= qty < 1000:
                return qty, 0.09
            elif 1000 <= qty <= 2000:
                return qty, 0.16
        except ValueError:
            print("Invalid order. Please enter a whole number for the quantity of logs.")


# Function to choose the shipping option and return its cost
def shipping_option():
    while True:
        try:
            option = int(input(
                "\nChoose the shipping option:\n"
                " 1 - Road Transport - $ 1000.00\n"
                " 2 - Rail Transport - $ 2000.00\n"
                " 3 - Waterway Transport - $ 2500.00\n"
                "Option: "
            ))
            if option == 1:
                return 1000
            elif option == 2:
                return 2000
            elif option == 3:
                return 2500
            else:
                print("Invalid option. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


# Execute functions and calculate the final order total
unit_price = choose_wood_type()
quantity, discount = log_quantity()
shipping_cost = shipping_option()

total = ((unit_price * quantity) * (1 - discount)) + shipping_cost

# Display final order total
print(f"\nTotal: $ {total:.2f}")