deposit = float(input("Deposit: "))  # Deposit input prompt

housing = round(0.25 * deposit, 2)
food = round(0.1 * deposit, 2)
transportation = round(0.15 * deposit, 2)

# housing = "{:.0%}".format(housing)
housingresult = "Housing: " + str(housing)
foodresult = "Food: " + str(food)
transportationresult = "Transportation: " + str(transportation)

print(housingresult)
print(foodresult)
print(transportationresult)
