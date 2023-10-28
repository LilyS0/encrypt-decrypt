#import
import random
import string

ALPHA_NUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
MAX_KEY_SIZE = 100

#function to create a key by adding random letters to a string
def create_key(message: str) -> str:

  """
  Right now it makes a key that is the same size as the message,
  in the future make it so that if the key size is limited by MAX_KEY_SIZE
  """
  
  #returns a string of random characters and digits 
  return ''.join((random.choice(ALPHA_NUM) for _ in message))
  

def get_values(message: str) -> list:
  
  #returns a list of the ascii values of a string
  return (ord(i) for i in message)



def combine_lists(list1: list, list2: list) -> list:

  #returns a list where each value is the combined value of every index in the two input lists
  return [((x + y)%126) for x,y in zip(list1, list2)]

def list_to_word(values_list: list) -> str:

  #returns a string that has the characters of each ascii value in the values_list at the corresponding index
  return ''.join(chr(i) for i in values_list)

def encrypt_word(message: str) -> tuple:

  #creates the key
  key = create_key(message)

  #returns key and encrypted word
  return key, list_to_word(combine_lists(get_values(key), get_values(message)))


def main():
  word = "hello"
  key, cypher_text = encrypt_word(word)

  print("Key: ", key, "\nEncrypted word: ", cypher_text)

if __name__ == "__main__":
  main()


  

 