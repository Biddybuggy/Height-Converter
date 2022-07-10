import math

#Getting user choice/input
choice = int(input("CHOICES \n1. cm to feet and inches \n2. Feet and inches to cm \nYour input: "))
if 1 <= choice <= 2:
    #Converting cm to feet and inches
    if choice == 1:
        cm_value = float(input("\nEnter height in cm: "))
        in_value = cm_value/2.54
        ft_value = in_value / 12
        ft = math.trunc(ft_value)
        inch = in_value - (ft*12)
        print(f"\nHeight in cm: {cm_value} cm \nHeight in feet and inches: {ft} ft {inch:.2f} in")

    #Convert feet and inches to cm
    elif choice == 2:
        ft_value = int(input("\nEnter ft value (e.g. if you're 5'7 enter 5): "))
        in_value = int(input("Enter in value (e.g. if you're 5'7 enter 7): "))
        inch = ft_value*12 + in_value
        cm = inch*2.54
        print(f"\nHeight in feet and inches: {ft_value} ft {in_value} in \nHeight in cm: {cm:.2f} cm")

else:
    print("\nInvalid input.")
