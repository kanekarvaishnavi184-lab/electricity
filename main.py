
# Electricity Bill Calculator

# Calculate electricity cost
def units_cost(units):
    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 7)


# Fixed charge
def fixed_charge():
    return 50


# Calculate total bill
def total_bill(units):
    return units_cost(units) + fixed_charge()


# NEW FEATURE: High consumption detection
def check_high_consumption(units):
    if units > 200:
        return "High Electricity Consumption!"
    else:
        return "Normal Electricity Consumption."


# Main function
def main():
    print("===== ELECTRICITY BILL CALCULATOR =====")

    try:
        units = float(input("Enter electricity units consumed: "))

        if not units.is_integer() or units < 0:
            print("Please enter a valid whole number.")
            return

        units = int(units)

        print("\n----- BILL DETAILS -----")
        print("Units Consumed:", units)
        print("Electricity Cost: Rs.", units_cost(units))
        print("Fixed Charge: Rs.", fixed_charge())
        print("Total Bill: Rs.", total_bill(units))
        print("Consumption Status:", check_high_consumption(units))

    except ValueError as e:
        print("Invalid Input:", e)


if __name__ == "__main__":
    main()