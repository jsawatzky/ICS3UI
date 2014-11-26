sentence = "I like to play with cats because cats are my friends."
print(sentence)

print("\n Let's now replace all instances of the word CATS with DRAGONS \n")


#First, we use the .split() function to split the sentence into an array of words
wordList = sentence.split()
print(wordList)

searchWord = "cats"
replacementWord = "dragons"


#The new sentence begins as an empty string, which we'll build up one word at a time
#using a for-loop
newSentence = ""

for i in range(0, len(wordList)):
      
      if wordList[i] == searchWord:
            wordList[i] = replacementWord

      newSentence = newSentence + " " + wordList[i]


print(newSentence)



