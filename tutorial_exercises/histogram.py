import sys
import random


def create_histogram(words_list):
    histogram = {}
    for word in words_list:
        if word not in histogram:
            histogram[word] = 1;
        else:
            histogram[word] += 1
    return histogram


def choose_random_word(histo):
    ran_index = random.randint(0, len(histo) - 1)
    return list(histo.keys())[ran_index]

def create_log(histo):
    new_log = {}
    for key in histo:
        new_log[key] = 0
    return new_log

def log_randomness(chosen_word, current_log):
    current_log[chosen_word] += 1

def get_frequencies(histo, token_num):
    frequency_dict = {}
    for key in histo:
        relative_probability = histo[key]/token_num
        frequency_dict[key] = relative_probability
    return frequency_dict

def create_word_range(frequency_dict):
    ''' updates the frequency dic
    by assigning each word a unique decimal range between
    withink 0 and 1 as a list to use in the stochastic chooser'''
    counter = 0
    for key in frequency_dict:
        chunk = [counter, frequency_dict[key] + counter]
        frequency_dict[key] = chunk
        counter = chunk[1]

def stochastic(frequency_dict):
    random_decimal = random.random()
    keys_list = list(frequency_dict.keys())
    while True:
        choice = keys_list[random.randint(0, len(keys_list)-1)]
        if (frequency_dict[choice][0] <= random_decimal <= frequency_dict[choice][1]):
            return choice



def first_order_mc(text_list, histo):
    markov = {}
    for key in histo:
        markov[key] = {}

    for index in range(len(text_list)-1):
        current_word = text_list[index]
        next_word = text_list[index + 1]
        if next_word in markov[current_word]:
            markov[current_word][next_word] += 1
        else:
            markov[current_word][next_word] = 1
    return markov

def make_sentence(num_of_words, mc_chain_dict):
    for _ in range(num_of_words):
        pass







''' __TESTS__ '''


larger_text = """and that this thought of the end and advantage is even
stronger than its strongest impulse not to be tempted to inexpedient
activities by its impulses that is its wisdom and inspiration In
comparison with the ignoble nature the higher nature is more
irrational for the noble magnanimous and self sacrificing person
succumbs in fact to his impulses and in his best moments his reason
lapses altogether An animal which at the risk of life protects its
young or in the pairing season follows the female where it meets with
death does not think of the risk and the death its reason pauses
likewise because its delight in its young or in the female and the
fear of being deprived of this delight dominate it exclusively it
becomes stupider than at other times like the noble and magnanimous
person He possesses feelings of pleasure and pain of such intensity
that the intellect must either be silent before them or yield itself to
their service his heart then goes into his head and one henceforth"""

larger_text.strip()
convert_to_array = larger_text.split()


suess = ['one', 'fish', 'two','fish','red','fish','blue','fish']
ex_histo = create_histogram(convert_to_array)
print(first_order_mc(convert_to_array, ex_histo))
hist_2 = create_histogram(suess)
print(first_order_mc(suess, hist_2))



# example_log = create_log(example_histo)
'''
for _ in range(10000):
    word = stochastic(ex_frequencies)
    log_randomness(word, example_log)
print(example_log)

'''
'''
example_histo = create_histogram(example_words)
example_log = create_log(example_histo)

for _ in range(2000):
    word = choose_random_word(example_histo)
    log_randomness(word, example_log)
print(example_log)
'''
