elements = {
    "H": 1.008,
    "He": 4.0026,
    "Li": 6.94,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "Na": 22.990,
    "Fe": 55.845
}

N = int(input("Скільки елементів потрібно додати? "))

for i in range(N):
    name = input("Введіть символ хімічного елемента: ")
    mass = float(input("Введіть атомну масу елемента: "))
    elements[name] = mass

sorted_elements = sorted(elements.items(), key=lambda item: item[1])

print("Елементи за зростанням атомної маси:")

for name, mass in sorted_elements:
    print(name, "-", mass)