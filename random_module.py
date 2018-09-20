import random

print(random.randint(0, 100)) # generate a random integer between 0 and 100

food = ['Raviolli', 'Pasta', 'Pizza', 'Cheesecake ']
print(random.choice(food)) # prints a random element from the list
print(random.shuffle(food)) # shuffles the list