#Arrays quiz
#Jacob Sawatzky

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days)

print("")

print(days[2])

print("")

for i in range(1, 5):
    print(days[i])

print("")

for i in range(0, len(days)*3):
    print(days[i%len(days)])

print("")

NikolasMarks = [80, 60, 30, 40, 20]
print("Nikolas Marks: " + str(NikolasMarks))

print("")

NikolasMarks.append(90)
print("Nikolas Marks: " + str(NikolasMarks))

print("")

for i in range(len(NikolasMarks)):
    NikolasMarks[i] += 15
print("Nikolas Marks: " + str(NikolasMarks))

print("")

lowestMark = 999
for i in NikolasMarks:
    if i < lowestMark:
        lowestMark = i
print("Lowest mark: " + str(lowestMark))

##OR

lowestMark = min(NikolasMarks)
print("Lowest mark (alt): " + str(lowestMark))

print("")

NikolasMarks.remove(lowestMark)
print("Nikolas Marks: " + str(NikolasMarks))

print("")

print("All done!")
