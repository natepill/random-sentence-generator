from flask import Flask
from random_sentence import *
from markov import MarkovChain

app = Flask(__name__)

@app.route('/')
def hello_world():
    markov = MarkovChain()
    dict = markov.build_markov()
    return markov.generate_sentence(dict)



if __name__ == "__main__":
    app.run(debug=True, port=33507)
