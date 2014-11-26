def getSlop(x1, y1, x2, y2):

      if x2-x1 == 0:
            slope = "Undefined"

      else:
            slope = (y2-y1)/(x2-x1)

      return slope

print("Here is a slope: " + str( getSlop(2, 6, 2,10)))
