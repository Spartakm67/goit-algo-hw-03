import random

def get_numbers_ticket(min, max, quantity):
    my_set = set()
    length = 0
    
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        print("Function parameters do not meet the specified constraints")
        lottery_numbers = []
        return lottery_numbers

    while length < quantity:
        num = random.randint(min, max)
        my_set.add(num)
        length = len(my_set)

    lottery_numbers = list(my_set)
    lottery_numbers.sort()
    print("Your lottery numbers: ", lottery_numbers)
    
    return lottery_numbers

get_numbers_ticket(1, 10, 11)
