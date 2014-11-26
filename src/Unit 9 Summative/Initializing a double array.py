cellContents = []

for i in range(0,3):
    currentRow = []
    
    for j in range(0,20):
        currentRow.append(0)
        
    cellContents.append( currentRow )


cellContents[2][6] = 1

print(cellContents)
