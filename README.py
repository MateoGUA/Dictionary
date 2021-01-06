# Dictionary
Dictionary application to practice

# Module 1: Load dictionary, tipology JSON, JavaScript Object Notation
import json
data = json.load(open("data.json")

# Module 2: Searching algorithm
def translate(word):
  word=word.lower()
  if word in data:
    return data(word)
  elif word.title() in data:
    return data(word.title())
  elif word.upper() in data:
    return data(word.upper())
  else:
    print("Sorry pal, not answer")

# Module 3: Generating formated answer
def format(output)
  if type output == list then:
    for item in output:
      print(item)
  else print(output)         
                 
# Module 4: User interaction
word = "word"                 
for word != "exit"
  word = input("Introduce your word: ")
  definition = translate(word)
  format(definition)
  print()
