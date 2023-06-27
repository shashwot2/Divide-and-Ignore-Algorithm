import random

def divide_and_ignore(input_list:list) -> list:
    if len(input_list) < 0:
        return input_list
    
    # Divide:
    mid = len(input_list) // 2

    #The python gods will decide which half to ignore
    ignored_half = random.choice([0,1])
    if ignored_half == 1:
        right = input_list[mid:]
        return right
    else:
        left = input_list[:mid]
        return left
     
