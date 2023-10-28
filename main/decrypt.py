from utils import *

def decrypt_word(key: str, message: str):

  
  #create integer lists from the message and key
  key_values = get_values(key)
  message_values = get_values(message)

  if(len(key) == len(message)):

    #subtract the two lists index by index
    subtracted_list = subtract_lists(message_values, key_values)
  
  else:

    num = len(message)/len(key)
    full_key_values = key_values*num
    subtracted_list = subtract_lists(message_values, full_key_values)

  #turns subtracted list into word
  result = list_to_word(subtracted_list)

  return result
  