chassisNum = input("Enter chassis number : ")

makerCode = chassisNum[:3].upper()

# print(makerCode)
match makerCode:
    case "MAT":
        print("Tata Motors")
        yearCode = chassisNum[9]
        monthCode = chassisNum[11]
        print(yearCode)
        print(monthCode)

    case "MB1":
        print("Ashok Leyland")
        yearCode = chassisNum[9]
        monthCode = chassisNum[11]
        print(yearCode)
        print(monthCode)

    case _:
        print("Chassis number data not available")