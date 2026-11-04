from datetime import date
import math
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

pi = math.pi
volume = (pi*(w**2)*a*(w*a + (2540*d)))/10000000000
print(f"The approximate volume is {volume:.2f}")
today = date.today()
with open("volumes.txt", "a") as file:
    file.write(f"{today}, {w}, {a}, {d}, {volume: .2f}\n")

# Additional feature
compare = input("Would you like to compare with another tire? (yes/no): ").lower()
if compare == "yes":
    print("\nEnter the second tire measurements")
    w2 = float(input("Enter the width: "))
    a2 = float(input("Enter the aspect ratio: "))
    d2 = float(input("Enter the diameter: "))
    volume2 = (math.pi * (w2**2) * a2 * (w2*a2 + 2540*d2)) / 10000000000
    print(f"\nFirst tire volume: {volume:.2f} liters")
    print(f"Second tire volume: {volume2:.2f} liters")
    if volume > volume2:
        difference = volume - volume2
        percentage = (difference / volume2) * 100
        print("The first tire has a larger volume.")
        print(f"Volume difference: {difference:.2f} liters")
        print(f"The first tire is {percentage:.2f}% larger.")

    elif volume2 > volume:
        difference = volume2 - volume
        percentage = (difference / volume) * 100

        print("The second tire has a larger volume.")
        print(f"Volume difference: {difference:.2f} liters")
        print(f"The second tire is {percentage:.2f}% larger.")

    else:
        print("Both tires have the same volume.")
    with open("volumes.txt", "a") as file:
        file.write(f"{today}, {w2}, {a2}, {d2}, {volume2:.2f}\n")