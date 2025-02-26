hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))


if hours > 40:
     overtime = hours - 40
     pay = round(40 * rate + overtime * rate * 1.5)
else:
     pay = round(hours * rate)
     
     
print(f"Pay: {pay: .2f}")


      
