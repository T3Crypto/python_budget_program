from ez_calculations import hcalc
from ez_calculations import fcalc
from ez_calculations import tcalc

deposit = float(input("Deposit: "))  # Deposit input prompt

print("Housing: " + str(round(deposit * hcalc, 2)))
print("Food: " + str(round(deposit * fcalc, 2)))
print("Transportation: " + str(round(deposit * tcalc, 2)))

# Version (1)
# deposit = float(input("Deposit: "))  # Deposit input prompt

# housing = float(input("Percentage for housing: "))
# food = float(input("Percentage for food: "))
# transportation = float(input("Percentage for transportation: "))

# hcalc = deposit * (housing / 100)
# fcalc = deposit * (food / 100)
# tcalc = deposit * (transportation / 100)

# hround = round(hcalc, 2)
# fround = round(fcalc, 2)
# tround = round(tcalc, 2)

# hresult = "Housing: " + str(hround)
# fresult = "Food: " + str(fround)
# tresult = "Transportation: " + str(tround)

# print(hresult)
# print(fresult)
# print(tresult)

# Version (2)
# deposit = float(input("Deposit: "))  # Entering Deposit amount

# housing = float(input("Percentage of housing: ")) / 100.0
# food = float(input("Percentage of food: ")) / 100.0
# transportation = float(input("Percentage of transportation: ")) / 100.0

# print("Housing: " + str(round(deposit * housing, 2)))
# print("Food: " + str(round(deposit * food, 2)))
# print("Transportation: " + str(round(deposit * transportation, 2)))
