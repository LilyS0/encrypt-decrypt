#import
import random
import string

ALPHA_NUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
MAX_KEY_SIZE = 100

#function to create a key by adding random letters to a string
def createKey(message: str) -> str:

  """
  Right now it makes a key that is the same size as the message,
  in the future make it so that if the key size is limited by MAX_KEY_SIZE
  """
  
  #returns a string of random characters and digits 
  return ''.join((random.choice(ALPHA_NUM) for _ in message))
  
def getValues(message: str):
  
  #returns a list of the ascii values of a string
  return (ord(i) for i in message)

def combine_lists (list1, list2):

  #returns a list where each value is the combined value of every index in the two input lists
  return [((x + y)%126) for x,y in zip(list1, list2)]

def encryptedWord (x):
  #turns numbers into letters a=1, b=2 c=3 ... 
  character = dict(enumerate(string.ascii_lowercase, 1))

  encryptedWordList = []
  for number in x:
    encryptedWordList.append(character[number])

  finalWord = ''.join(encryptedWordList)  

  return finalWord

def encryptFunction(baseWord):


#takes out spaces
  newBaseWord = baseWord.replace(" ","" )

  key = createKey(newBaseWord)

  baseWordValues = getValues(newBaseWord)

  keyValues = getValues(key)

  encryptedWordList = combinedLists(baseWordValues, keyValues)

  return key, encryptedWord(encryptedWordList)
 