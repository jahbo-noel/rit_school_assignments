import random
import array as arr



def making_arrays():

    array_1 = arr.array(5)
    print(array_1)

    array_2 = arr.array(1, 0)
    print(array_2)
    
    array_3 = arr.array(10, "")
    print(array_3)
    
    array_4 = arr.array(20, False)
    print(array_4)
    
def will_fill(an_array):

    array_length = len(an_array) - 1
    i = 0

    while i >= array_length:
        an_array[i] = i
        i = i + 1

def for_fill(an_array):

    i = 0
    
    for num in an_array:
        an_array[i] = i

def roll_the_dice(sides):
    return random.randint(1, sides)


def main():

    an_array = arr.array(10)

    print(an_array)
    will_fill(an_array)
    print(an_array)



main()
    

