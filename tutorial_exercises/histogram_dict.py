import sys

'''
A histogram() function which takes a source_text argument
(can be either a filename or the contents of the file as a string,
your choice) and return a histogram data structure that stores
each unique word along with the number of times the word appears
in the source text.
'''
def create_file_string(filename):
    ''' Takes in a text file and returns all
    of its contents in a string '''
    with open(filename, 'r') as f:
        #array_of_lines = []
        #for line in f:
            #line = line.lower()
            # remove whitespace from end of the
            # line and add it to the array
            #array_of_lines.append(line.strip())
            #string_of_contents = "".join(array_of_lines)
            string_of_contents = f.read()

    return string_of_contents

print(create_file_string('joyful_wisdom.txt'))

#def histogram(filename):
    #with open(filename, 'r') as f:
        #string_of_contents = f.read(1000)
        #string_of_contents = string_of_contents.replace("\n", " ")
        #return string_of_contents




'''
A unique_words() function that takes a histogram argument and
returns the total count of unique words in the histogram. For example,
when given the histogram for The Adventures of Sherlock Holmes,
it returns the integer 8475.
'''

def unique_words():
    pass

'''
A frequency() function that takes a word and histogram argument
and returns the number of times that word appears in a text.
For example, when given the word "mystery" and the Holmes histogram,
it will return the integer 20.
'''

def frequency():
    pass
