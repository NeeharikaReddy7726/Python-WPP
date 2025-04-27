# Conve
conversion_factors = [12, 1/3, 1/5280, 304.8, 30.48, 0.3048, 0.0003048]
conversion_units = ["Inches", "Yards", "Miles", "Millimeters", "Centimeters", "Meters", "Kilometers"]

feet = float(input("Enter length in feet: "))
print("Choose a conversion option:")
print("1: Inches\n2: Yards\n3: Miles\n4: Millimeters\n5: Centimeters\n6: Meters\n7: Kilometers")

choice = int(input("Enter the corresponding number (1-7): "))

if 1 <= choice <= 7:
    converted_value = feet * conversion_factors[choice - 1]
    print(f"{feet} feet is {converted_value} {conversion_units[choice - 1]}.")
else:
    print("Invalid choice. Please enter a number between 1 and 7.")