distance = float(input("Enter the distance"))
choice = int(input("Choose a conversion (1 or 2): "))
if choice == 1:
    miles = distance * 0.621371
    print(distance, "kilometers=" , miles, "miles")
elif choice == 2:
    kilometers = distance * 1.60934
    print(distance, "miles =", kilometers,"kilometers")
else:
    print("Invalid Choice")
