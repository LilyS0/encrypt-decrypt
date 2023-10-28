from utils import *

def decrypt_word(key: str, message: str):

  if(len(key) == len(message)):
    #create integer lists from the message and key
    key_values = get_values(key)
    message_values = get_values(message)

    #subtract the two lists index by index
    subtracted_list = subtract_lists(message_values, key_values)

    #turns subtracted list into word
    result = list_to_word(subtracted_list)

    return result
  
  else:
    #repeat the key len(message)/len(key) times over the string to decrypt
    pass