#EXAMPLE OF A NESTED FOR LOOP

#MULTIPLES OF 2

for rowNumber in range(6,15): #THE OUTER LOOP
      rowText = ""

      for multiplier in range(1,11): #THE INNER LOOP
            entry = rowNumber * multiplier
            rowText = rowText + str(entry) + "\t"

      print(rowText)

