# Exception Handling
x = int(input("Enter a Number: "))
try:
    y = 5/x
except ZeroDivisionError:
    print("Not Allowed To Divide by Zero!")
except:
    print("Error Occurred but not determined")
else:
    print(f"No Error Occurred.\
The Final Result is {y}")
finally:
    print("Program Finished")
