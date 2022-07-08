import random

with open("templates.txt") as file:
    phrases = file.readlines()


inputs = {'noun': input("Enter a noun"),
          'verb': input("Enter a past tense verb"),
          'adjective': input("Enter an adjective"),
          'adverb': input("Enter an adverb")}

chosen = random.choice(phrases)

splitPhrase = chosen.split(" ")

for index in range(0, len(splitPhrase)):
    if "[noun]" in splitPhrase[index]:
        splitPhrase[index] = inputs['noun']
    elif "[verb]" in splitPhrase[index]:
        splitPhrase[index] = inputs['verb']
    elif "[adjective]" in splitPhrase[index]:
        splitPhrase[index] = inputs['adjective']
    elif "[adverb]" in splitPhrase[index]:
        splitPhrase[index] = inputs['adverb']

finalPhrase = ""
for word in splitPhrase:
    finalPhrase = finalPhrase + " " + str(word)

print(finalPhrase)

