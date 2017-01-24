# Premienanie z Farenheitov na Kelviny
# Vstup v F
farenheit = float(input("Zadajte teplotu v F: "))
#farenheit = int(farenheit)

# Premeň F -> K
kelvin = ((farenheit * 9) / 5 + 32) + 273.15

# Vypíš K
print("Stupne K: {}".format(kelvin))
