regNums = ["RJ14AB1234", "INVALID", "RJ27CD5678", "RJ45EF9999"]

for regNum in regNums:
    if regNum == "INVALID":
        print("INVALID REG NUMBER SKIPPED")
        continue

    print("PROCESSING : ", regNum)


transactions = [1200, 4500, 9999, 150000, 3200]

for amount in transactions:
    if amount >= 100000:
        print("BUSINESS TRANSACTION FOUND : ", amount)
        break

    print("PERSONAL TRANSACTION : ", amount)