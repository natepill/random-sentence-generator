from flask import Flask
from markov import MarkovChain, generate_lincoln_tweet

app = Flask(__name__)


# Art of War
# Confusious text
# How to Win Friends or Influence People
# Any Robert Greene book, ie: 48 laws of Power


@app.route('/')
def hello_world():
    markov = MarkovChain('harry_potter_7.txt')
    dict = markov.build_markov()
    return markov.create_sentence(dict)



if __name__ == "__main__":
    app.run(debug=True, port=4000)
