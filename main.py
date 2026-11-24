
# Electricity Bill Calculator

# Function to calculate electricity cost
def units_cost(units):
    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 7)


# Function to calculate fixed charge
def fixed_charge():
    return 50


# Function to calculate total bill
def total_bill(units):
    return units_cost(units) + fixed_charge()


# Main function
def main():
    print("===== ELECTRICITY BILL CALCULATOR =====")

    try:
        units = float(input("Enter electricity units consumed: "))

        if not units.is_integer():
            print("Please enter a whole number of units.")
            return

        units = int(units)

        if units < 0:
            print("Units cannot be negative.")
            return

        print("\n----- BILL DETAILS -----")
        print("Units Consumed:", units)
        print("Electricity Cost: Rs.", units_cost(units))
        print("Fixed Charge: Rs.", fixed_charge())
        print("Total Electricity Bill: Rs.", total_bill(units))

    except ValueError as e:
        print("Invalid Input:", e)


# Execute main function
if __name__ == "__main__":
    main()