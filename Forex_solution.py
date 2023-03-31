import requests 

from_currency = str(
    input("Enter in the currency you'd like to conver from: ")).upper()

to_currency = str(
    input("Enter in the currency you'd like to convert to: ")).upper()

amount = float(input("Enter in the amount of money: "))

response = requests.get(
    f"http://api.frankfurter.app/latest?amount={amount}&from={from_currency}&tp={to_currency}")

print(
    f"{amount} {from_currency} is {response.json()['rates'][to_currency]} {to_currency}")