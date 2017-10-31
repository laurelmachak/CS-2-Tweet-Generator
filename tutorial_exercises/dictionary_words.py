import random
import sys



def sentence_gen(num_of_words):
    ran_sentence = ""
    with open('/usr/share/dict/words', 'r') as f:
        array = f.readlines()
        f.close()
    for _ in range(num_of_words):
        ran_index = random.randint(0, len(array)-1)
        word = str(array[ran_index]).strip()
        ran_sentence += (word + " ")
        del array[ran_index]
    ran_sentence.strip()
    return ran_sentence

if __name__ == "__main__":
    print(sentence_gen(int(sys.argv[1])))
