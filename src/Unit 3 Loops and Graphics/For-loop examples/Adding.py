#Add 1+2+3+...+20

total = 0

maxNum = int(input("Enter how many integers you want to add up: "))

for n in range(1, maxNum+1):
      
      dollarAmount = float(input("Enter a dollar amount to add: "))
      total = total + dollarAmount
      roundedTotal = round( total, 2)
      print("Total is now " + str(roundedTotal))

      
