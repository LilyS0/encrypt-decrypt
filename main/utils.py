def get_values(message: str) -> list:
  
    #returns a list of the ascii values of a string
    return [ord(i) for i in message]

def add_lists(list1: list, list2: list) -> list:

    #returns a list where each value is the combined value of every index in the two input lists
    return [((x + y)%126) for x,y in zip(list1, list2)]

def subtract_lists(list1: list, list2: list) -> list:

    #returns a list where each value is the subtracted value of every index in the two input lists
    return [make_positive(x-y) for x,y in zip(list1, list2)]

def list_to_word(values_list: list) -> str:

    #returns a string that has the characters of each ascii value in the values_list at the corresponding index
    return ''.join(chr(i) for i in values_list)

def make_positive(num: int) -> int:

    #if the number is less than 0 add 126 to make it in range for chr()
    if num < 0:
        return num + 126
    return num

def find_highest_factor(num: int) -> int:

    #initialize result
    result = 0

    #loop through every number 1-num to find the highest factor that is not itself
    for i in range(1, num+1):
        if num%i == 0 and i > result and i != num:
            result = i
    
    #if num is prime it will just return the number instead of 1
    if result == 1:
        return num
    
    return result

