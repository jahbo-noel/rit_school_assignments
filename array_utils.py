import random
import array 

def random_array(size, min_value=0, max_value=None):

    an_array = array.array(size, 0)

    if max_value is None:
        max_value = size

    for i in range(size):
        an_array[i] = random.randint(min_value, max_value)

    return an_array

def main():

    random_array(10, min_value=0, max_value=None)

main()
