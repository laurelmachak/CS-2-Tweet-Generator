import random
import sys

def create_words_list(filename):
    with open(filename, 'r') as f:
        array = f.readlines()
    return array

def sentence_gen(num_of_words, array):
    ''' inputs, what it does, what it returns '''
    ran_sentence = ""

    for _ in range(num_of_words):
        ran_index = random.randint(0, len(array)-1)
        word = str(array[ran_index]).strip()
        ran_sentence += (word + " ")
        del array[ran_index] #sampling w/o replacement
    ran_sentence.strip()
    return ran_sentence

if __name__ == "__main__":
    list_of_words = create_words_list('/usr/share/dict/words')
    number_of_words = int(sys.argv[1])
    num_of_sentences = int(sys.argv[2])
    for _ in range(num_of_sentences):
        print(sentence_gen(number_of_words, list_of_words))
