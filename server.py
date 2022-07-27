from flask import Flask
from random import randint

random_number = randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home_page():
    return '<h1> Guess a number between 0 and 9 </h1>' \
           '<iframe src="https://giphy.com/embed/777Aby0ZetYE8" width="480" height="259"' \
           'class="giphy-embed" </iframe>' \


# Creating variable path and converting the path to a specific data type


@app.route("/<int:number>")
def guess_number(number):

    if number > random_number:
        return '<h1 style="color: #A93226">Too high, try again!</h1>' \
               '<iframe src="https://giphy.com/embed/2cei8MJiL2OWga5XoC" width="480" height="270" frameBorder="0"' \
               'class="giphy-embed" allowFullScreen</iframe>'

    elif number < random_number:
        return '<h1 style="color: #E74C3C">Too low, try again!</h1>' \
               '<iframe src="https://giphy.com/embed/yMBRzjqgS0penXtdQT" width="480" height="270" frameBorder="0"' \
               'class="giphy-embed" allowFullScreen </iframe>'

    else:
        return '<h1 style="color: #196F3D">You found me!</h1>' \
               '<iframe src="https://giphy.com/embed/cXblnKXr2BQOaYnTni" width="480" height="270" ' \
               'frameBorder="0" class="giphy-embed" allowFullScreen></iframe>' \



if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
