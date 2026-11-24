from main import units_cost, fixed_charge, total_bill, check_high_consumption

def test_units_cost():
    assert units_cost(50) == 150
    assert units_cost(150) == 550
    assert units_cost(250) == 1150

def test_fixed_charge():
    assert fixed_charge() == 50

def test_total_bill():
    assert total_bill(100) == 350

def test_high_consumption():
    assert check_high_consumption(250) == "High Electricity Consumption!"

def test_normal_consumption():
    assert check_high_consumption(150) == "Normal Electricity Consumption."