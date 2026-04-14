import random

# інший варіант задачі 2

def get_numbers_ticket(min, max, quantity):
        
    if min < 1 or max > 1000 or min > max or quantity < 1 or quantity > (max - min + 1):
        print("Function parameters do not meet the specified constraints")
        lottery_numbers = []
        return lottery_numbers

    lottery_numbers = random.sample(range(min, max + 1), quantity)

    lottery_numbers.sort()

    print("Your lottery numbers: ", lottery_numbers)
    
    return lottery_numbers

get_numbers_ticket(1, 1000, 6)
