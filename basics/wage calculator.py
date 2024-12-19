startHour = int(input("Enter the starting hour: "))
startMin = int(input("Enter the minute: "))
endHour = int(input("Enter the ending hour: "))
endMin = int(input("Enter the ending minute: "))
payRate = int(input("Enter the hourly pay: "))
minutes = (endMin+startMin)/60
hours = (endHour-startHour)
overallPay = hours*payRate
print (f"worked from {startHour}:{startMin:02d} to {endHour}:{endMin:02d}")
print(f"Time spent: {hours+minutes} hours")
print(f"{overallPay}")

