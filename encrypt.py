#import
import random
import string

#function to create a key by adding random letters to a string
def createKey(message: str):
  #starts a string of random numbers
  randomLetter= ('')

  #creates a list of random letters
  list1 = [randomLetter]
  for _ in message:

    #gets random letter
    randomLetter= random.choice('abcdefghijklmnopqrstuvwxyz')
    
    #adding each random letter to the list
    list1.append(randomLetter)
    #joins the list
    decoderKey = ''.join(list1)
  
  return decoderKey
  
def getValues(x):
  #dict to turn letters into values working wierd? not correct values
  values = dict()
  for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

  valuesList=[]
  for character in x:
    valuesList.append(values[character])
  
  return valuesList

def combinedLists (list1, list2):
  encryptedWordList = [x + y for x,y in zip(list1, list2)]

  modEncryptList = []
  for number in encryptedWordList:
    output = (number % 27)
    if (number > 26):
      modEncryptList.append(output + 1)
    else:
      modEncryptList.append(output)
    
  return modEncryptList

def encryptedWord (x):
  #turns numbers into letters a=1, b=2 c=3 ... 
  character = dict(enumerate(string.ascii_lowercase, 1))

  encryptedWordList = []
  for number in x:
    encryptedWordList.append(character[number])

  finalWord = ''.join(encryptedWordList)  

  return finalWord

def encryptFunction():
#the message to be encrypted
  baseWord = input("Enter your message to be encrpyted: ")

#takes out spaces
  newBaseWord = baseWord.replace(" ","" )

  key = createKey(newBaseWord)

  baseWordValues = getValues(newBaseWord)

  keyValues = getValues(key)

  encryptedWordList = combinedLists(baseWordValues, keyValues)


  print('your key is '+ key)

  print('Your Encrpyted Word is ' + encryptedWord(encryptedWordList))   