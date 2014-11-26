

for rowNumber in range(1,60):
      rowText = ""

      for multiple in range(1,11):
            entry = rowNumber * multiple
            rowText = rowText + str(entry) + "\t"

      print(rowText)
