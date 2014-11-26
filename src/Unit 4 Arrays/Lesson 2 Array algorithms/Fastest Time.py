raceTimes = [453, 450, 420, 492, 509, 444, 460, 530, 499]

fastestTime = raceTimes[0]

for i in range(0, len(raceTimes)):
      if raceTimes[i] < fastestTime:
            fastestTime = raceTimes[i]

print(fastestTime)

#Remove the fastest time from the list

raceTimes.remove( fastestTime )

print(raceTimes)

fastestTime = raceTimes[0]

for i in range(0, len(raceTimes)):
      if raceTimes[i] < fastestTime:
            fastestTime = raceTimes[i]

print(fastestTime)
      
