from flask import Flask, render_template
import histogram

app = Flask(__name__)

@app.route('/')
def index():
    #example_words = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish'];
    example_words = histogram.convert_to_array
    example_histo = histogram.create_histogram(example_words)
    tokens = len(example_words)
    ex_frequencies = histogram.get_frequencies(example_histo, tokens)
    histogram.create_word_range(ex_frequencies)
    random_word = histogram.stochastic(ex_frequencies)
    return render_template('index.html', random_word=random_word)



if __name__ == "__main__":
    app.run(debug=True)


# http://127.0.0.1:5000/
