import random
import sys

def rearrange_words(array):
    ''' scramble words from an array '''
    new_string = ""
    for _ in range(len(array)):
        ran_index = random.randint(0, len(array) -1)
        new_string += (str(array[ran_index]) + " ")
        del array[ran_index]
    new_string.strip()
    return new_string

if __name__ == "__main__":
    print(rearrange_words(sys.argv[1:]))
