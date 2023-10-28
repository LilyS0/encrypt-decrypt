#import
import random
from utils import *

ALPHA_NUM = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
MAX_KEY_SIZE = 20

#function to create a key by adding random letters to a string
def create_key(message: str) -> str:

  """
  Right now it makes a key that is the same size as the message,
  in the future make it so that if the key size is limited by MAX_KEY_SIZE

  if the len of message < MAX_KEY_SIZE
    make the key the size of message 
  else
    make the key the size of the highest factor of the len of the message
  """
  
  
  #returns a string of random characters and digits 
  return ''.join((random.choice(ALPHA_NUM) for _ in message))
  

def encrypt_word(message: str) -> tuple:

  """
  Needs to be updated to support messages that are longer than the key

  if len(key) = len(message)
    proceed as usual
  else
    repeate the key len(message)/len(key) times over the message to encrypt
  """

  #creates the key
  key = create_key(message)

  #creates integer lists from message and key
  key_values = get_values(key)
  message_values = get_values(message)

  #adds the values at each index and puts it in a list
  combined_values = add_lists(key_values, message_values)

  #creates a string from the values of the combined lists
  result = list_to_word(combined_values)

  #returns key and encrypted word
  return key, result



  

 