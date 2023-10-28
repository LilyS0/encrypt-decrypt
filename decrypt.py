#import
import string 

#fucntion that gets the values of each letter in a word
def getValues(x):
  #dict to turn letters into values working wierd? not correct values
  values = dict()
  for index, letter in enumerate(string.ascii_letters):
   values[letter] = index + 1

  #makes a list to add the values to
  valuesList=[]
  #adds each value to a list
  for character in x:
    valuesList.append(values[character])
  
  return valuesList

#takes 2 lists and subtracts each place from each other. ex. [1,2,3,4] [5,4,3,2,1] 1 - 5, 2 - 4, ...
def combinedLists (list1, list2):
  encryptedWordList = [x - y for x,y in zip(list1, list2)]

  #makes a list to add numbers to
  modEncryptList = []
  #takes each number from encryptedWordList and if the number is below one it loops it bake to 26
  for number in encryptedWordList:
    if (number < 1):
      number = 26 - abs(number)
    modEncryptList.append(number)
    
  return modEncryptList

#take a list of numbers and turns it into characters
def decryptedWord(numberList):
  character = dict(enumerate(string.ascii_lowercase, 1))
  decryptWordList = []

  for number in numberList:
    decryptWordList.append(character[number])
  
  finalWord = ''.join(decryptWordList)

  return finalWord

#function that uses all previous functions to decrypt a word 
def decryptFunction():
  #imputs
  encryptedWord = input('Enter encrypted word: ')
  key = input('Enter the key: ')

  #get values of the encrypted word and key
  encryptWordValues = getValues(encryptedWord)
  keyValues = getValues(key)

  #subtracts the values of the 2 value lists above
  combinedList = combinedLists(encryptWordValues, keyValues)

  #converts the numbers from the list above into the decrypted word
  finalWord = decryptedWord(combinedList)

  print ('The decrypted message is: ' + finalWord)