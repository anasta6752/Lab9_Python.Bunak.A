countries = []

for i in range(10):
    country = input(f"Введіть назву країни №{i + 1}: ")
    countries.append(country)

countries = tuple(countries)

print("Кортеж країн Європи:")
print(countries)
