chassisNum = input("Enter chassis number : ")

if(len(chassisNum < 17)):
    print("Invalid chassis number")
    exit()

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