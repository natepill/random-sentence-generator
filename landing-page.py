from flask import Flask, render_template

app = Flask(__name__)

# Art of War
# Confusious text
# How to Win Friends or Influence People
# Any Robert Greene book


@app.route('/', methods=['GET'])
def landing_page():
    # return '<html><body><h1> Hello World </h1></body></html>'
    return render_template('index.html')

if __name__ == "__main__":
   app.run(debug = True)
