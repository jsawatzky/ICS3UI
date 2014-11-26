i = 0
p = ["a","b","c","d","e","f"]
phrase = ["YOU", "ARE", "NOT", "IT"]

while len(p) > 1:

      print("")
      print(p)

      for w in phrase:
            print( p[i] + " " + w )
            if  w != "IT":
                  i = (i+1) % len(p)
      
      p.remove( p[i] )

      if i == len(p):
            i = 0

print( p[0] + " wins")

            
