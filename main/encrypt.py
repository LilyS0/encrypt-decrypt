#import
import random
from utils import *

ALPHA_NUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
MAX_KEY_SIZE = 20

#function to create a key by adding random letters to a string
def create_key(message: str) -> str:

  message_len = len(message)

  if(message_len <= MAX_KEY_SIZE):

    #returns a string of random characters and digits that is the size of the message
    return ''.join((random.choice(ALPHA_NUM) for _ in message))
  
  else:

    #finds the highest factor of the size of the message to make the key length
    key_len = find_highest_factor(message_len)

    #returns a string of random characters and digits that is the size of key_len
    return ''.join((random.choice(ALPHA_NUM) for _ in range(key_len)))

  

def encrypt_word(message: str) -> tuple:

  #creates the key
  key = create_key(message)

  

  #creates integer lists from message and key
  key_values = get_values(key)
  message_values = get_values(message)

  if(len(key) == len(message)):
    #adds the values at each index and puts it in a list
    combined_values = add_lists(key_values, message_values)
  
  else:
    num = len(message)/len(key)
    full_key_values = key_values*num
    combined_values = add_lists(full_key_values, message_values)

  #creates a string from the values of the combined lists
  result = list_to_word(combined_values)

  #returns key and encrypted word
  return key, result




  

 