print("On average how many sesame seeds are on a Big Mac?")

guess = input("What is your guess: ")
while guess != "380" and guess != "give up":
    print("Incorrect!")
    guess = input("What is next your guess: ")

if guess == "380":
    print("Correct! Congragulations!")
else:
    print("Better luck next time.")
    


