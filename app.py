from flask import Flask
from random_sentence import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    text_list = text_to_list('blog-text')
    return generate_sentence(text_list)


if __name__ == "__main__":
    app.run(debug=True, port=33507)
