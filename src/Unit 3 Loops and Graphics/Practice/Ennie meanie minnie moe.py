i = 0
p = ["a", "b", "c", "d", "e", "f", "g", "h"]
phrase = ["You", "are", "not", "it"]
w = phrase[0]

while len(p) > 1:
    for w in phrase:
        print(p[i] + ": " + w)
        if i < len(p)-1: i = i+1
        else: i = 0
    i -= 1
    print(p[i] + " is out")
    p.remove(p[i])
    print(i, len(p))
    if i == len(p): i = 0
print(p[0] + " wins")
