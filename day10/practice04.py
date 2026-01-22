chassisNum = input("Please enter the chassis number : ")


if(len(chassisNum) < 17):
    print("Invalid chassis number")
    exit()

def checkChassis(chassisNum):
    makerCode = chassisNum[:3].upper()

    match makerCode:
        case "MAT":
            return checkTataMotors()
        case "MB1":
            return checkAshokLeyland()
        
            
        case _:
            print("Chassis number data not available")

def checkTataMotors():
            print("Manfacturer is Tata Motors")
            yearCode = chassisNum[9]
            monthCode = chassisNum[11]
            print(yearCode)
            print(monthCode)

def checkAshokLeyland():
            print("Manfacturer is Ashok Leyland")
            yearCode = chassisNum[9]
            monthCode = chassisNum[11]
            print(yearCode)
            print(monthCode)

            

checkChassis(chassisNum)

